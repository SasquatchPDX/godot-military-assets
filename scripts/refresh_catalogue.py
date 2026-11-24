"""Refresh the approved publisher index or check links in the curated README."""

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import html
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = "https://tevy.dev"
CATEGORIES = {
    "Aircraft": {"aircraft", "helicopter", "turboprop"},
    "Watercraft": {"ship", "tugboat", "cargo ship", "container ship", "patrol boat"},
    "Ground vehicles": {"ambulance", "forklift", "utility vehicle", "cargo truck", "fuel truck"},
    "Environments": {"aircraft hangar", "airfield", "guard tower", "port office", "ship-to-shore"},
    "Props": {"jerrycan", "shipping container", "cargo pallet", "sandbag", "medical kit"},
}
PUBLISHER_CATEGORIES = {
    "Aircraft": "vehicles",
    "Watercraft": "vehicles",
    "Ground vehicles": "vehicles",
    "Environments": "buildings",
    "Props": "props",
}
USER_AGENT = "GodotMilitaryAssets/1.0 (+https://github.com/SasquatchPDX/godot-military-assets)"


def refresh_index():
    request = Request(f"{PUBLISHER}/models.json", headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=30) as response:
        feed = json.load(response)
    if feed["schema"] != 1 or feed["site"] != PUBLISHER or feed["count"] != len(feed["models"]):
        raise ValueError("Unexpected publisher index format or count")

    groups = defaultdict(list)
    for model in feed["models"]:
        slug = model["slug"]
        if model["license"] != "CC0-1.0" or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            continue
        tags = {tag.lower() for tag in model["tags"]}
        for category, accepted_tags in CATEGORIES.items():
            if model["category"] == PUBLISHER_CATEGORIES[category] and tags & accepted_tags:
                break
        else:
            if model["category"] == "vehicles" and "military" in tags:
                category = "Ground vehicles"
            else:
                continue
        version = model["version"]
        if not isinstance(version, int) or version < 1:
            continue
        files = [
            (entry["lod"], entry["path"])
            for entry in model["files"]
            if isinstance(entry["lod"], int)
            and entry["lod"] >= 0
            and entry["path"] == f"/models/{slug}/v{version}/lod{entry['lod']}.glb"
        ]
        if not files:
            continue
        # Escape all punctuation that could be rendered as Markdown or HTML.
        title = re.sub(r"[^\w ./,-]", lambda match: f"&#{ord(match[0])};", " ".join(model["name"].split()))
        downloads = " · ".join(f"[LOD {lod}]({PUBLISHER}{path})" for lod, path in sorted(files))
        groups[category].append((slug, f"| [{title}]({PUBLISHER}/models/{slug}) | {downloads} |"))

    if not groups:
        raise ValueError("No catalogue matches. Leaving the previous index intact.")

    lines = [
        "# tevy asset index",
        "",
        "This index uses publisher tags to find CC0 visual models for transport, logistics, and related scenes.",
        "The GLBs use meshopt compression and KTX2 textures. Decode the required extensions before importing into stock Godot 4.6.",
        "",
        "[Publisher formats and license](https://tevy.dev/docs) · [Curated catalogue](README.md)",
        "",
    ]
    for category in CATEGORIES:
        if groups[category]:
            lines.extend([f"## {category}", "", "| Publisher page | Version-pinned GLB downloads |", "|---|---|"])
            lines.extend(row for _, row in sorted(groups[category]))
            lines.append("")
    (ROOT / "PUBLISHER-INDEX.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Indexed {sum(map(len, groups.values()))} publisher listings.")


def check_link(url):
    request = Request(url, headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"})
    try:
        with urlopen(request, timeout=12):
            return None
    except HTTPError as error:
        return url, f"HTTP {error.code}"
    except (OSError, URLError):
        return url, "Connection failed"


def check_links():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    urls = sorted(set(re.findall(r'https://[^\s<>"|\])]+', readme)))
    with ThreadPoolExecutor(max_workers=8) as executor:
        failures = [result for result in executor.map(check_link, urls) if result]
    missing = [(url, reason) for url, reason in failures if reason in {"HTTP 404", "HTTP 410"}]
    inconclusive = len(failures) - len(missing)
    summary = [
        "## Curated catalogue links",
        "",
        f"Checked {len(urls)} URLs. Missing responses: {len(missing)}. Other inconclusive responses: {inconclusive}.",
        "",
    ]
    summary.extend(f"- {reason} · <{html.escape(url)}>" for url, reason in missing)
    report = "\n".join(summary) + "\n"
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as destination:
            destination.write(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-links", action="store_true")
    if parser.parse_args().check_links:
        check_links()
    else:
        refresh_index()
