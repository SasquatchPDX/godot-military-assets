# Godot Military Assets

A catalogue of military and transport game art for Godot projects, with publisher links, file formats, and listed license terms. The catalogue covers fictional and historical vehicles, characters, environments, props, textures, and audio.

- [Model collections](#1-high-priority-model-collections)
- [Named aircraft, ground vehicles, and vessels](#2-named-model-leads)
- [DCS leads requiring permissions](#3-dcs-crossover-candidates--permission-and-source-files-required)
- [Godot import checklist](#4-import-and-asset-library-checklist)
- [Additional collections and historical sources](#expansion-2--additional-model-collections-and-source-geometry)
- [Newer listings by asset type](#expansion-3--additional-game-assets-by-type)
- [tevy publisher index with version-pinned GLB downloads](PUBLISHER-INDEX.md)

To suggest an asset, [open an issue](https://github.com/SasquatchPDX/godot-military-assets/issues/new) with the publisher URL, file formats, license or usage terms, and the category it belongs in.

## 1. High-priority model collections

| Collection | Download URL | Formats / license / scope |
|---|---|---|
| Motion Mistry military model collection | https://motionmistry.pk/3d-models/ | 48 GLB models listed; aircraft, ships, vehicles; individual creator attribution, many CC BY 4.0; verify original license |
| Vinish military vehicle collection | https://vinish.dev/free-3d-models/military-vehicles | GLB, glTF, OBJ; four fictional vehicles: tank, APC, patrol vehicle, truck; CC BY 4.0 |
| Quaternius Animated Tanks | https://quaternius.com/packs/animatedtanks.html | Four animated low-poly tanks, FBX/OBJ/Blend, CC0 |
| Quaternius Ships | https://quaternius.com/packs/ships.html | Stylized civilian/historical boats, FBX/OBJ/Blend, CC0 |
| Quaternius all packs | https://quaternius.com/ | Transport, buildings, animated characters, scenery; check individual pack |
| OpenGameArt CC0 vehicle collection | https://opengameart.org/content/cc0-3d-vehicles-and-cars | Individual downloadable entries: Abrams, reconnaissance tank, MiG, patrol boat, submarine, technical, military off-road vehicle, trucks and merchant ships |
| OpenGameArt CC0 3D collection | https://opengameart.org/content/3d-assets-cc0 | Vehicles and scenery; check each entry |
| Low-Poly Military Kit Free | https://heyheythere.itch.io/low-poly-military-kit-free | Historical lead. Former Godot-oriented CC BY 4.0 sampler with GLB, FBX, OBJ and Blend. Publisher page returned 404 on 24 November 2026. |
| FlightGear FGAddon | https://wiki.flightgear.org/FGAddon | Approximately 500 aircraft of all types, not all military; source meshes typically need conversion; GPL and per-file license checks |
| FlightGear model gallery | https://wiki.flightgear.org/Table_of_models | Individual aircraft links and previews |
| AMVLab Aircraft Models | https://github.com/amvlab/aircraft-models | GLB, CC BY 4.0: A320, A350, A380, B737, B787, drone and eVTOL; civilian background assets |
| FPS Buildings Environment Kit | https://github.com/petroulacl/fps-buildings-env-kit | CC0 collection of buildings, roads, scenery and PBR materials; inspect upstream notices |
| TurboSquid free military models | https://www.turbosquid.com/Search/3D-Models/military?free=true | Marketplace index; mixed formats and licenses; account may be necessary |
| 3D Valley | https://3dvalley.com/3d-models | General CC0 model aggregator; GLB; verify upstream license |

## 2. Named model leads

The following names are indexed on the source pages; use their individual download buttons. A named lead does not imply that geometry is accurate or animated.

### Aircraft

- Motion Mistry: F-35, B-2, JAS 39 Gripen (including Ukrainian livery variant). https://motionmistry.pk/3d-models/
- FlightGear: Buccaneer, A-4, A-6E, F-8, F-14, Hawker Sea Hawk, A-10, B-52, E-3, F-15C, F-80C, Harrier, F-16, T-37, Mirage F1, Mirage 2000-5, T-38, OV-10A, J35F Draken, HAL Tejas, F-22, MiG-29, PC-9M, PC-21, V-22. https://wiki.flightgear.org/Table_of_models
- OpenGameArt: MiG model. https://opengameart.org/content/cc0-3d-vehicles-and-cars

### Ground

- Vinish: fictional MBT, 8x8 APC, 4x4 patrol vehicle, 6x6 cargo truck. https://vinish.dev/free-3d-models/military-vehicles
- Quaternius: four stylized animated tank models. https://quaternius.com/packs/animatedtanks.html
- OpenGameArt: Abrams, reconnaissance tank, technical, Soviet military off-road vehicle, trucks. https://opengameart.org/content/cc0-3d-vehicles-and-cars

### Sea

- Motion Mistry: Gerald R. Ford carrier, Arleigh Burke destroyer, Type 22 Houbei, coast guard ship, container ship, research ship, submarine. https://motionmistry.pk/3d-models/
- OpenGameArt: patrol boat, submarine, container ships, icebreaker, dredger, steamer. https://opengameart.org/content/cc0-3d-vehicles-and-cars

## 3. DCS crossover candidates — permission and source files required

These are leads, NOT cleared Godot assets. An open-source code license may not cover meshes or textures. Ask the artist for original Blender/FBX/glTF files and explicit reuse permission if terms are unclear.

| Project | URL | Status |
|---|---|---|
| Community A-4E-C | https://github.com/heclak/community-a4e-c | Check separate art terms and availability of original meshes |
| UH-60L | https://github.com/Kinkkujuustovoileipa/uh-60l | Same |
| SK60 | https://github.com/BAAS-Dynamic/DCS-SK60-Mod | Same |
| Vietnam War Vessels | https://github.com/tspindler-cms/tetet-vwv | Same |
| WWII Royal Navy | https://github.com/ErrantKnight-Modding/WWII-Royal-Navy-Assets/releases | Check original artist rights |
| Currenthill | https://www.currenthill.com/ | Publisher explicitly prohibits redistribution without permission |
| VSN | https://filedn.eu/ldmvNCjOtAfkbhMFc1BTA2f/VSN_html_Links/VSN_MODS.html | Unclear source and license; not cleared |
| Massun92 | https://forum.dcs.world/topic/316316-massun92s-asset-pack-official-update-march-2024/ | Request source and permission |
| MAM | https://files.digitalcombatsimulator.com/en/files/filter/user-is-BlackLibrary/apply/ | Request source and permission |

DCS Make Flyable is not a source of independently reusable geometry. Do not assume proprietary EDM files can be imported into Godot or that extraction is authorized.

## 4. Import and asset library checklist

- Prefer GLB/glTF; use Blender for FBX, OBJ, Blend and authorized legacy meshes. Godot import docs: https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html
- Keep original archives and license/attribution files separate from processed assets.
- Check texture paths, material appearance, scale (metres), pivot orientation, normals, and animation clips.
- Generate visual LODs and lightweight collision shapes for tabletop, mobile and web rendering. Share meshes and materials among repeated visual instances.
- Record source URL, creator, license, original file name, revision, model format, triangle count, texture sizes, and permission status for each asset.
- CC0 is generally simplest; CC BY requires credit and indication of changes; GPL and other copyleft assets require separate distribution review. Marketplace terms vary. Do not treat a free download as a blanket license.

## 5. Suggested priority

Start with the GLB collection and CC0 vehicle packs for fast prototypes, then FlightGear for recognizable historical aircraft, and finally approach DCS artists for high-detail source meshes. No claim is made that the DCS crossover assets are legally reusable or technically importable as distributed.

## Expansion 2 — additional model collections and source geometry

| Collection | Download URL | Format / licensing / scope |
|---|---|---|
| Spring: 1944 | https://github.com/spring1944/spring1944 | WWII RTS source assets across German, Italian, Japanese, Hungarian, British, Soviet, US and Swedish factions; infantry, vehicles, aircraft and boats. Conversion and per-file license audit required. |
| FlightGear shared models | https://wiki.flightgear.org/Shared_models | Additional scenery beyond aircraft: naval vessels, support vehicles, structures. Legacy inventory; locate current source files and license before reuse. |
| tevy military transport | https://tevy.dev/models/military-transport | Original generic turboprop aircraft, CC0, GLB, three LODs and separate movable parts. The publisher files require meshopt decoding for stock Godot 4.6. |
| tevy transport LOD0 | https://tevy.dev/models/military-transport/v1/lod0.glb | Publisher's version-pinned direct GLB URL; 2 MB, 72,466 triangles. |
| Steelfront free sampler | https://bluefrost-lowpoly.itch.io/steelfront-free-sampler | Seven low-poly models and one effect, LODs, animations, collision; commercial use advertised. |
| Steelfront additional packs | https://itch.io/game-assets/new-and-popular/genre-strategy/tag-military | Index of low-cost tank, naval, fixed-wing and building packs; glTF/FBX; inspect each license. |
| Army Pack – Cute Series | https://rg-poly.itch.io/army-pack-cute-series | 96-model free sampler, 300+ paid models including color variants; CC0, glTF and FBX. Stylized, not realistic. |
| Artiquea modern military RTS pack | https://artiquea.itch.io/low-poly-military-rts-pack | 69 models, €10 listed, GLB/FBX/OBJ/Blend, royalty-free game use; no raw asset redistribution. |
| Epicapple free military collection | https://sketchfab.com/epicapple/collections/free-military-6018d1bcb7114f77a451309c67c190c0 | 35-model curated collection including carriers and frigate. Inspect each license and provenance; exclude unauthorized game rips. |
| Sketchfab military aircraft | https://sketchfab.com/tags/military-aircraft | Search index; filter downloadable, check each original creator and license. |
| NASA 3D Resources | https://science.nasa.gov/3d-resources/ | Aircraft, spacecraft and infrastructure reference models; NASA media usage rules apply. |
| Smithsonian Open Access 3D | https://www.si.edu/spotlight/3d-objects?edan_fq%5B0%5D=media_usage%3A%22CC0%22 | CC0 museum scans, including Bell X-1 and Wright Flyer; historical reference and museum scenes. |
| Smithsonian bulk GLB mirror | https://huggingface.co/datasets/hugging-3d/smithsonian-open-access-3d | 3,451 general museum packages, 22.3 GB; only a small subset is aviation-related; third-party mirror, confirm provenance. |
| Meshy military vehicle index | https://www.meshy.ai/subcategory/military-vehicles | Large AI-generated model discovery index; advertised 12,950+ listings, not unique verified game-ready models. Check rights, geometry and accuracy individually. |
| Unity Military FREE pack | https://assetstore.unity.com/packages/3d/environments/military-free-low-poly-3d-models-pack-260358 | 30 advertised assets; publisher lists Godot/GLTF support; confirm specific license and obtain engine-independent distribution before use. |

### FlightGear shared scenery leads

- CG-57 cruiser, LPD-17 landing platform dock, Oliver Hazard Perry frigate, Clemenceau carrier, fuel truck, tow tractor, Humvee pickup, barracks and shelters. Source inventory: https://wiki.flightgear.org/Shared_models
- Historical aircraft gallery: https://wiki.flightgear.org/Aircraft — Beaufighter, Fokker Dr.I, P-51D, A6M2, Ki-84, Fw 190, Sopwith Camel, Spitfire, MiG-15, F4U and Bf 109.

These are visual game assets and reference sources, not validated engineering models. Godot imports and archive-level licensing remain unverified for these listings. Counts are publisher listings, may include variants and duplicates. Paid collections are explicitly labeled. Preserve author, source URL and asset-specific license metadata.

## Expansion 3 — additional game assets by type

Publisher listings checked on 24 November 2026. The Godot versions below reflect publisher documentation.

### Characters and animation

| Asset | Access and terms | Formats and coverage |
|---|---|---|
| [CSAF Fort Vale and Foxhole bundle](https://csaf.itch.io/fort-vale-psx-soldiers) | Paid with free samples. Commercial game use and modification permitted. Standalone redistribution prohibited. AI-assisted. | Modern and Second World War soldiers, plus civilian and other characters on a shared skeleton. GLB, FBX, OBJ, Blend and a PSX shader. Publisher tested in Godot 4.7.2. [Foxhole is also sold separately](https://csaf.itch.io/foxhole-psx-ww2-soldiers). |
| [Synty POLYGON Military Pack](https://syntystore.com/products/polygon-military-pack) | Paid under the [Synty store EULA](https://syntystore.com/pages/one-time-purchase-licence), with seat limits. | Native Godot 4.6.2+ project and FBX source. Soldiers, pilots, civilians, vehicles and modular desert buildings. Characters come without animation clips. |
| [Quaternius Ultimate Animated Character Pack](https://quaternius.com/packs/ultimatedanimatedcharacter) | Free, CC0. | 52 stylized characters for background populations and prototyping. FBX, OBJ and Blend. [Creator's OpenGameArt upload](https://opengameart.org/content/animated-characters-pack). |
| [Quaternius Universal Animation Library](https://quaternius.com/packs/universalanimationlibrary.html) | CC0. Free subset and paid full/source tiers. | Humanoid animation clips for retargeting, including walks, runs, sitting and swimming. GLB and FBX. The source tier includes the rigged Blend file. |
| [Kenney Mini Characters](https://kenney.nl/assets/mini-characters) | Free, CC0. | Animated low-poly characters for civilian and support roles. |
| [Kenney Animated Characters 1](https://opengameart.org/content/animated-characters-1) | Free, CC0. | Stylized survivor and zombie skins for a shared FBX character, plus separate idle, run and jump animation files. |
| [World War 2 US Helmets by vmatthew](https://sketchfab.com/3d-models/world-war-2-us-helmets-156b75501004472ea192ced70619e6f4) | Free, Sketchfab lists CC Attribution. | Downloadable US helmet variants for period characters. About 137,000 triangles across the listing and 4K textures. |

### Ground vehicles

| Asset | Access and terms | Formats and coverage |
|---|---|---|
| [Zsky Low Poly Military Vehicles](https://zsky2000.itch.io/low-poly-military-vehicles) | Pay what you want, CC BY 4.0 on itch.io. Poly Pizza lists CC BY 3.0 for its edition. | Nine stylized models in FBX, OBJ and Blend. [GLB edition on Poly Pizza](https://poly.pizza/bundle/Low-Poly-Military-Vehicles-lSgBuYh48X). |
| [Newc42 Low Poly German WWII Tanks](https://newc-42.itch.io/german-low-poly-wwii-tanks) | Pay what you want, CC0. | Three stylized historical exterior meshes, Leichttraktor, Panzer III J and Tiger I, in FBX and Blend. |
| [ReignFallStudio K511A1 Cargo Truck](https://reignfallstudio.itch.io/k511a1-military-truck) | Paid. Commercial use permitted with limits on raw redistribution. AI-assisted engine integration. | Logistics truck with Godot 4 package, FBX and Blender source, animation and collision meshes. |
| [Game Retro Studio Military Jeep](https://game-retro-studio.itch.io/military-jeep) | Paid. Publisher permits commercial project use. | PSX-style Willys MB in GLB, FBX and OBJ. |
| [Kenney Car Kit](https://kenney-assets.itch.io/car-kit) | Free, CC0. | GLB/glTF, FBX and OBJ. Civilian and support vehicles including vans, trucks and an ambulance. |
| [singam96 PSX Military Vehicle Pack](https://singam96.itch.io/psx-military-vehicle-pack) | Paid. Personal and commercial projects allowed. Standalone redistribution prohibited. AI-assisted. | 50 fictional GLBs with baked textures, interiors and animation clips. Includes ambulances, recovery vehicles, cargo trucks and armored vehicles. |
| [Sneznyj Voxel Police & Military](https://sneznyj.itch.io/voxel-police-military) | Paid. Personal and commercial use with restrictions on redistribution. AI-assisted. | 30 blocky vehicles, including an ambulance, hauler and utility vans. GLB, FBX and Blend. |
| [Artiquea Modern Military RTS Pack Vol. 2](https://artiquea.itch.io/low-poly-military-rts-pack-2) | Paid. Game-project use permitted. Raw asset redistribution restricted. | 73 stylized ground, air and maritime models in GLB, FBX, OBJ and Blend. |

### Aircraft and vessels

| Asset | Access and terms | Formats and coverage |
|---|---|---|
| [Mehozavr An-2](https://opengameart.org/content/an-2-airplane-lowpoly) | Free, CC0. | Low-poly An-2 biplane with Soviet military and Aeroflot liveries. Downloaded archive includes FBX, Blend, PNG and PSD. |
| [tevy Twin-Engine Utility Helicopter](https://tevy.dev/models/utility-helicopter) | Free, CC0. | Generic utility helicopter in three GLB LODs. Meshopt decoding needed for stock Godot 4.6. |
| [tevy Harbour Tug](https://tevy.dev/models/tugboat) and [Container Ship](https://tevy.dev/models/container-ship) | Free, CC0. | Port and merchant shipping models in three GLB LODs per model. Meshopt decoding needed for stock Godot 4.6. |
| [Reodesuxz Low Poly Airport Pack](https://reodesuxz.itch.io/low-poly-airport-pack) | Free. Personal and commercial project use. Standalone redistribution prohibited. | 22 stylized aircraft, support vehicles and airfield models. GLB, FBX, OBJ and Blend. |
| [Reodesuxz Low Poly Harbor Pack](https://reodesuxz.itch.io/low-poly-harbor-pack) | Free. Personal and commercial project use. Standalone redistribution prohibited. | 30 boats, dock pieces and port structures. GLB, FBX, OBJ and Blend. |
| [Kenney Watercraft Kit](https://kenney.nl/assets/watercraft-kit) | Free, CC0. | Publisher lists 45 stylized watercraft and related models. Downloaded archive includes GLB, FBX and OBJ. |
| [Scottish Maritime Museum CC0 collection](https://sketchfab.com/ScottishMaritimeMuseum/collections/scottish-maritime-museum-cc0-b367fa03fcea40279a5470eea7872709) | Free, CC0 on the linked model pages. Check the license of each additional model. | Detailed scans include [Air Sea Rescue Craft ASR-10](https://sketchfab.com/3d-models/air-sea-rescue-craft-asr-10-7f54d6af39674fb88f43bd48af3944c5) and [MV Spartan](https://sketchfab.com/3d-models/mv-spartan-e2c3ced464f14e3b864f15871bf6d87d). The linked vessels are roughly 500,000 triangles each and are candidates for mesh reduction. |
| [Poly Haven Smuggler's Cove](https://polyhaven.com/collections/smugglers_cove) | Free, CC0. | Seventeenth-century ships, fort and harbor scenery. Individual glTF or Blender downloads, including a [Dutch ship](https://polyhaven.com/a/dutch_ship_medium). |

### Environments and props

| Asset | Access and terms | Formats and coverage |
|---|---|---|
| [Zsky Low Poly Military Base Pack](https://zsky2000.itch.io/military-base-pack) | Pay what you want, CC BY 4.0. | Over 20 stylized assets including quarters and a medic tent. The publisher page does not specify mesh formats. |
| [Nailfighter LowPoly Modular Assets](https://nailfighter.itch.io/low-poly-bunker-modular-assets) | Free, CC0. | Bunker-style walls, floor tiles, crates and barrels. FBX and Blend with textures. |
| [dgv-dev PSX WWII Airfield and Hangar Kit](https://dgv-dev.itch.io/psx-wwii-airfield-hangar) | Paid. License terms are in the archive. AI-assisted. | 49 modular models including hangar, tower, runway tiles and equipment. GLB, FBX, OBJ, Blend and a Godot 4 demo. |
| [Greanapple Aviation Hangar Pack](https://greanapple.itch.io/aviation-hangar-pack) | Pay what you want. Personal and commercial use permitted. AI-assisted. | Hangar, apron tiles and a light aircraft. GLB and FBX, 1K PBR textures, two LODs and Godot collision nodes. |
| [Steelfront Base Buildings](https://bluefrost-lowpoly.itch.io/steelfront-base-buildings-pack) | Paid. Commercial use allowed with restrictions on standalone redistribution. | Nine animated RTS buildings including depot, barracks and hangar, plus modular runway pieces. glTF and FBX with LODs. |
| [Quarantine Zone 3D](https://haotianhuang.itch.io/quarantine-zone-3d) | CC0. Free 22-model GLB sampler and paid full pack. AI-assisted. | Modular fictional field hospital with tents, medical props and a helipad. Full pack has 103 models, GLB/FBX/OBJ and a Godot GridMap MeshLibrary. |
| [LowBitLab PSX Harbor Docks & Warehouse](https://lowbitlab.itch.io/psx-harbor-docks-warehouse) | Paid with sample. Free and commercial game use allowed. Standalone redistribution prohibited. | 99 PSX props and modules, including pier, warehouse, freight yard, crane and forklift. GLB, FBX, OBJ/MTL and Blend. |
| [Kenney City Kit Industrial](https://kenney.nl/assets/city-kit-industrial) | Free, CC0. | 40 stylized industrial assets including warehouses and factory buildings. |
| [Kenney Factory Kit](https://opengameart.org/content/factory-kit) | Free, CC0. | Industrial and warehouse props including conveyors. GLB, FBX and OBJ. |
| [tevy Harbour Container Crane](https://tevy.dev/models/harbour-crane) | Free, CC0. | Container crane with three GLB LODs and separate visual moving parts. Meshopt decoding needed for stock Godot 4.6. |
| [Poly Haven Wooden Military Crate](https://polyhaven.com/a/wooden_military_crate), [Metal Jerrycan Green](https://polyhaven.com/a/metal_jerrycan_green) and [Vintage Radio Transceiver](https://polyhaven.com/a/vintage_radio_transceiver) | Free, CC0. | Textured logistics and set-dressing props with glTF downloads. |

### Textures, effects and audio

| Asset | Access and terms | Formats and coverage |
|---|---|---|
| [SnowyCocoon Camouflage Texture Pack](https://store.godotengine.org/asset/snowycocoon/camouflage-texture-pack/) | Free, CC0. | Image-only pattern pack at 128 px to 2K. The store labels the package version unstable. |
| [Poly Haven Worn Asphalt](https://polyhaven.com/a/worn_asphalt) and [Freight Station](https://polyhaven.com/a/freight_station) | Free, CC0. | PBR paving surface and freight-yard HDRI for ports, aprons and depots. |
| [Kenney Particle Pack](https://kenney.nl/assets/particle-pack) | Free, CC0. | 80 particle textures for dust, mist and other atmosphere. |
| [Nayckron Heavy Vehicle Engine Loop](https://opengameart.org/content/engine-loop-heavy-vehicletank) | Free under listed CC BY 3.0 or GPL 3.0 terms. | WAV, OGG and MP3. The full archive has four speed variations. |
| [Sonniss GameAudioGDC](https://sonniss.com/gameaudiogdc/) | Free. Project use allowed under publisher terms, with standalone redistribution restricted. | Large WAV bundles with tracklists for finding vehicle and warehouse ambience. |

In Godot 4.6, GLB/glTF is the recommended interchange format. New FBX imports use ufbx by default. OBJ is useful for static meshes, and direct Blend import requires Blender. [Godot 4.6 import formats](https://docs.godotengine.org/en/4.6/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html).
