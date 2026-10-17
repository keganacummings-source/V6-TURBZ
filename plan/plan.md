# V6-TURBZ — Class Rebuild, Sprite Revamp & Move/FX Update

A large content update for the existing V6-TURBZ game: every character gets redrawn pixel sprites, and every class is rebuilt around its own playstyle gimmick with all-new perks.
It also adds 50+ complex moves with new gear and effects, a better Verses menu, and a new custom-build class. The result is handed over as a zip of the updated files.

## Who it's for
- The game's owner, who will add the files to GitHub themselves.
- Players who want each class to play differently, not just change its numbers.

## Core features and experience

**1. Sprite revamp (every class, same level of rework)**
- All character sprites are redrawn in pixel style. Each character keeps its current design, colours and silhouette.
- Melee classes get more defined, heavier bodies with clear weapons and melee poses, so they read as melee at a glance.
- Non-melee classes get the same level of polish without changing their look.
- The uploaded cat sprite sheet is used for the cat form, and the rabbit sheet for the Moonhopper form.

**2. Class rebuild: one real gimmick per class**
- Every class loses its old perks and gets a new, unique perk set built around its gimmick. Examples:
  - **Spirit class:** an aura that makes her spirits follow the mouse cursor.
  - **Blink class:** double-click anywhere on the map to teleport there, with a cooldown.
  - **Phantom class:** a 20-second ghost mode. While in it, she can only damage enemy ghosts and only takes damage from enemy ghosts.
  - **Cat-shift class:** turns into a cat with 4x movement speed.
  - **Boss-eater class:** turns into bosses it has killed. It keeps a catalog of them and you pick a form from that catalog.
  - **Moonhopper:** turns into a rabbit with an aura and hops around the map.
- Any other classes get gimmicks of the same scale, matched to their current theme.

**3. New class: the Crying Girl (custom build)**
- A new pixel sprite of a crying Japanese girl.
- The player builds her loadout by picking perks from one list that has every new perk plus all the old legacy perks.

**4. Move, gear and FX update**
- 50+ new complex moves (combos, dashes, multi-hit, area, projectile and status moves), spread across all classes as signature moves.
- New gear pieces that change or boost those moves.
- New pixel-style effects: hit sparks, trails, auras and transformation bursts.

**5. Verses menu refinement**
- Filter characters by role: melee, ranged, magic, support.
- Filter by effect type (for example burn, freeze, teleport, transform, summon, ghost).
- Filters can be combined, and the visible list updates right away.

**6. Delivery**
- One zip containing only the changed and new files. Files that weren't touched are left out.
- Each file sits at its exact path from the project root, the same as in the repo. The zip can be dragged straight onto GitHub and the files land where they belong.

## User flow
1. Open the game, then go to the Verses menu.
2. Filter by role and/or effect, then pick a character (or the Crying Girl).
3. For the Crying Girl, open her build screen and choose perks from the new and legacy lists.
4. In a match, use the class gimmick (aura, double-click teleport, ghost mode, transform) and the new signature moves.
5. The boss-eater opens its catalog to choose a boss form.

## UI/UX feel
- Everything stays pixel art and matches the game's current look. No smooth or painted art.
- Melee sprites look bold and weighty. Effects are punchy but stay readable.
- Verses filters are compact pixel-style toggle chips placed above the character grid.

## Implementation phases
**Phase 1 (MVP, built now)**
- Revamped pixel sprites for every existing class, with melee classes reworked the most.
- Every class rebuilt with a unique gimmick and all-new perks, including the six examples above.
- The Crying Girl class with a custom build and a combined new and legacy perk list.
- 50+ new moves spread across the classes, plus new gear and effects.
- Verses menu role and effect filters.
- A zip of only the changed and new files, at their proper repo paths.

**Phase 2**
- Balance pass on gimmicks and moves based on play feedback.
- Saved presets for Crying Girl builds.
- More animation frames (idle and hit variants) for the transform forms.

**Phase 3**
- Extra skins per class.
- More boss forms added to the boss-eater catalog.
- An in-game move and gimmick tutorial for each class.

## Assumptions
- Classes are rebuilt inside the existing game's code and engine. No new platform or framework is added.
- Old perks are removed from the regular classes and kept only inside the Crying Girl's perk list.
- Gimmicks are given to the classes that fit them best by theme. Any classes left over get new gimmicks invented at the same scale.
- Gimmicks have cooldowns or time limits so they don't stay active forever (the ghost mode lasts 20 seconds).
- Sprites are made in-house in pixel style to match the current art. The uploaded cat and rabbit sheets are used as provided.
- Effect filter categories come from the effects the new moves and perks actually use.
- The folder structure inside the zip matches the uploaded V6-TURBZ-main project. There is no extra wrapper folder, so the paths line up when the files are dragged onto GitHub.
- Nothing is deleted from the repo. Old perks are removed by editing files, not by deleting them.
