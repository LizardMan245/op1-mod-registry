# OP-1 mod registry

Which names and numbers each mod for the original OP-1 (firmware 246) adds, so mods, and the sounds
made with them, don't clash.

The list is [`registry.json`](registry.json); the tables below are made from it. If you make a mod
for 246, add yours: see [Add or correct an entry](#add-or-correct-an-entry).

## Why it matters

Without a shared list, names collide sooner than anyone expects. On the M-VAVE FM-1, where firmware
modding took off at the same time, at least six firmwares in its installer hub carry the same identity,
`FM-1_900`, and "two firmwares with the same identity look like one"
([dinghy's guide](https://github.com/zvenson/dinghy/blob/main/docs/MAKE-IT-YOURS.md),
[the hub's catalog](https://fm1.designburgapps.com/catalog.json), October 2026). This list is here so the
OP-1 doesn't go the same way.

- **Sounds store names.** A saved sound says `"fx_type": "nitro"`, `"type": "digital"`,
  `"lfo_type": "element"`. If two mods use one name for different things, each plays the other's
  sounds wrong. The names are the IDs that matter most.
- **Unknown names.** Stock 246 crashes on a sound that names an effect or engine it doesn't have, so
  a sound made with one mod can stop stock or another mod. The last table says what each firmware does.
- **Rows.** The effect, engine, LFO and sequencer lists are rows in `content/op1_factory.db`. A row
  number is only used inside one firmware, so rows matter when mods go into one build: a combined
  build, a configurator, plugins.
- **Everything else** a mod takes (a marker for engines in iter's slot, key combinations, MIDI
  messages, files, firmware bytes, memory) can't be taken twice in one build either.

<!-- tables:start -->

### Projects

| project | by | version | note |
|---|---|---|---|
| stock 246 | Teenage Engineering | 246 |  |
| [op1r](https://github.com/pcppcp/op1r) | popcorp | op1r 35 (1eadb87) |  |
| [Opus](https://opus-op1.pages.dev) | LizardMan | 2 beta 1 (build 1, core 2.7) | a core and plugins: each feature a file (.opmod) in /mods on the USB disk; a row naming a plugin (opus.NAME) is there only while its file is. Effect rows are added by name when the effect list first opens, and a row whose type neither the OS nor a loaded plugin knows is deleted then (op1r's too, unless the bridge runs that effect). Engines run in iter's slot. The bridge (opus.bridge, beside the starter pack) runs op1r's .op1p and Hundekraft's .knl files with their own names and op1r's numbers |
| [Oblique Strategies](https://github.com/ultralazr/op1-oblique-strategies) | ultralazr | 1a2f2fe |  |
| [Squarewave Studio](https://squarewave.studio) | Joseph Holland | in development | names registered before release; rows, markers, keys and the rest come with its release |

### Effects (`fx_types`)

Sounds store the effect's name. The row is its row in `content/op1_factory.db`.

| name | row | project | note |
|---|---|---|---|
| grid | 3 | stock 246 |  |
| punch | 4 | stock 246 |  |
| delay | 5 | stock 246 |  |
| phone | 7 | stock 246 |  |
| spring | 8 | stock 246 |  |
| cwo | 9 | stock 246 |  |
| nitro | 10 | stock 246 |  |
| filter | 2 | op1r | stock's hidden 4-pole filter: stock plays it but doesn't list it |
| tape | - | op1r | tape echo; a plugin file (since op1r 34): its row is added at start-up (11 with all of op1r's plugins on a stock database) |
| clouds | - | op1r | a plugin file (since op1r 34): its row is added at start-up (12 with all of op1r's plugins on a stock database) |
| reverb | - | op1r | its screen says "Kali"; a plugin file (since op1r 34): its row is added at start-up (13 with all of op1r's plugins on a stock database) |
| palme | - | op1r | Musica Obscura by ultralazr; Ondes Martenot diffuseur; a plugin file (since op1r 34): its row is added at start-up (14 with all of op1r's plugins on a stock database) |
| in a room | - | op1r | Musica Obscura by ultralazr; Lucier's I am sitting in a room. Sounds saved as "sitting" (test builds) load as it; a plugin file (since op1r 34): its row is added at start-up (15 with all of op1r's plugins on a stock database) |
| filter | - | Opus | the OS's hidden filter, listed by opus.filter; row added when the effect list first opens (14 on a stock database with the whole pack, 11 on one that ran Opus 1) |
| bitcrush | - | Opus | opus.bitcrush; row added when the effect list first opens (11 on a stock database with the whole pack, 12 on one that ran Opus 1) |
| chorus | - | Opus | opus.chorus; row added when the effect list first opens (12 on a stock database with the whole pack, 13 on one that ran Opus 1) |
| plate | - | Opus | a reverb, opus.plate; row added when the effect list first opens (13 on a stock database with the whole pack, 14 on one that ran Opus 1) |

### Synth engines (`synth_types`)

Sounds store the engine's name as `type`.

| name | row | project | note |
|---|---|---|---|
| cluster | 1 | stock 246 |  |
| digital | 2 | stock 246 |  |
| drwave | 3 | stock 246 |  |
| fm | 4 | stock 246 |  |
| phase | 5 | stock 246 |  |
| pulse | 6 | stock 246 |  |
| dna | 7 | stock 246 |  |
| string | 8 | stock 246 |  |
| dsynth | 9 | stock 246 |  |
| voltage | 10 | stock 246 |  |
| iter | 11 | op1r | stock's hidden engine: stock has its code but no row |
| supersaw | - | op1r | a plugin file (since op1r 34): its row is added at start-up (12 with all of op1r's plugins on a stock database) |
| fmbell | - | op1r | a plugin file (since op1r 34): its row is added at start-up (13 with all of op1r's plugins on a stock database) |
| granular | - | op1r | a plugin file (since op1r 34): its row is added at start-up (14 with all of op1r's plugins on a stock database) |
| strata | - | Squarewave Studio | in development |
| mixtur | - | op1r | Musica Obscura by ultralazr; Mixtur-Trautonium undertones; a plugin file (since op1r 34): its row is added at start-up (15 with all of op1r's plugins on a stock database) |
| arc | - | op1r | Musica Obscura by ultralazr; Duddell's singing arc; a plugin file (since op1r 34): its row is added at start-up (16 with all of op1r's plugins on a stock database) |
| aether | - | op1r | a tilt theremin (the motion sensor), since op1r 33; a plugin file (since op1r 34): its row is added at start-up (17 with all of op1r's plugins on a stock database) |
| iter | 11 | Opus | the OS's hidden engine in the engine list with opus.iter: its row 11 added when the engine list loads, deleted at start without the plugin (op1r uses that row too). Opus's engines run in its slot either way |
| dimension | - | Opus | opus.dimension; in the engine list, no row: runs in iter's slot, mark 0x4F01 |
| amp | - | Opus | a guitar amp, opus.amp; in the engine list, no row: runs in iter's slot, mark 0x4F02 |
| dx | - | Opus | a DX7 voice player, opus.dx; in the engine list, no row: runs in iter's slot, mark 0x3B0D |
| outatime | - | Opus | opus.outatime; in the engine list, no row: runs in iter's slot, mark 0x29D4 |

### Engines and effects hosted in another's slot

A mod can run its engines in the slot of iter, stock's hidden engine, and its effects in the slot of the hidden filter. Their sounds then say `"type": "iter"` (or `"fx_type": "filter"`), so each mod marks which one a sound is for. Record where the mark goes and its values, so two mods don't use the same one.

| marker | where | engine or effect | project |
|---|---|---|---|
| synth 21249 (0x5300 + 1) | knobs[4] of a sound with "type": "iter" | supersaw | op1r |
| synth 21250 (0x5300 + 2) | knobs[4] of a sound with "type": "iter" | fmbell | op1r |
| synth 21251 (0x5300 + 3) | knobs[4] of a sound with "type": "iter" | granular | op1r |
| synth 21256 (0x5300 + 8) | knobs[4] of a sound with "type": "iter" | mixtur | op1r |
| synth 21257 (0x5300 + 9) | knobs[4] of a sound with "type": "iter" | arc | op1r |
| synth 21258 (0x5300 + 10) | knobs[4] of a sound with "type": "iter" | aether | op1r |
| FX 21249 (0x5300 + 1) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | tape | op1r |
| FX 21250 (0x5300 + 2) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | clouds | op1r |
| FX 21251 (0x5300 + 3) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | reverb | op1r |
| FX 21254 (0x5300 + 6) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | palme | op1r |
| FX 21255 (0x5300 + 7) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | in a room | op1r |
| 0x5300 + 4 … 7 (synth), 0x5300 + 4, 5 (FX) | reserved in op1r-src synth_sdk/plugins/ORDERS.md | Hundekraft's workshop engines and effects (wavetable, taffy, pew, elg; washer, snowglobe) | op1r |
| 0x5300 + 32 … 63 (synth and FX) | knobs[4], as above | plugin files without a number of their own: each OP-1 gives them one at start-up and keeps it (op1.db, table op1rplugins). 1 … 31 are for the numbers in ORDERS.md | op1r |
| 0x4F01 | knobs[4] of a sound with "type": "iter" | dimension | Opus |
| 0x4F02 | knobs[4] of a sound with "type": "iter" | amp | Opus |
| 0x3B0D (15117) | knobs[4] of a sound with "type": "iter" | dx | Opus |
| 0x29D4 (10708) | knobs[4] of a sound with "type": "iter" | outatime | Opus |
| 0x0100-0x7FFF, never 0x4Fxx or 0x53xx | knobs[4] of a sound with "type": "iter"; its "opus" member names the plugin | any Opus 2 plugin's engine: FNV-1a of the plugin's ID, ':' and the engine's name, folded to 15 bits (the same on every OP-1); op1r's engines through the bridge keep op1r's 0x5300 + n | Opus |
| FX 0x0100-0x7FFF, never 0x53xx | knobs[4] of an effect with "fx_type": "filter" | an effect a plugin runs in the filter's slot without a number of its own: the same hash of the plugin's ID and the effect's name; op1r's effects through the bridge keep op1r's 0x5300 + n | Opus |

### Drum engines (`drum_types`)

| name | row | project | note |
|---|---|---|---|
| dbox | 1 | stock 246 |  |
| gin | - | Squarewave Studio | in development |
| drum+ | 2 | op1r | since op1r 30 |

### LFOs (`lfo_types`)

| name | row | project | note |
|---|---|---|---|
| tremolo | 1 | stock 246 |  |
| value | 2 | stock 246 |  |
| random | 3 | stock 246 |  |
| element | 4 | stock 246 |  |
| midi | 5 | stock 246 |  |
| bend | 6 | stock 246 |  |
| crank | 7 | stock 246 |  |
| quad | 8 | op1r | four LFOs |
| matrix | - | Squarewave Studio | in development; working name |

### Sequencers (`seq_types`)

| name | row | project | note |
|---|---|---|---|
| pattern | 1 | stock 246 |  |
| endless | 2 | stock 246 |  |
| tombola | 3 | stock 246 |  |
| finger | 4 | stock 246 |  |
| sketch | 5 | stock 246 |  |
| arpeggio | 6 | stock 246 |  |
| euclid | 7 | op1r |  |
| dots | 8 | op1r |  |
| orbital | - | Squarewave Studio | in development |
| oracle | 9 | op1r | Musica Obscura by ultralazr; geomancy shield chart. "shield" (test builds) maps to it |
| peal | 10 | op1r | Musica Obscura by ultralazr; change ringing |

### Keys added inside sound files

Sounds are JSON. Record any key a mod adds, so two mods don't use one key for different things.

| key | what | project |
|---|---|---|
| op1r | drum+'s settings per pad, in a drum kit (since op1r 30); stock loads the kit as a normal drum | op1r |
| opus | Opus's member: "v" and "uses" (the plugins a sound needs, by plugin ID with its data's version, e.g. "opus.dimension": 1); "engine" (the plugin whose engine runs in iter's slot); "held" (the sound's own envelope and LFO while an engine holds the OS's); "engine_data" (an engine's own data, hex); a second effect's record under its manager's prefix: Fx overdrive's fx2_type (by name), fx2_active, fx2_params | Opus |

### Key combinations

Combinations a mod takes outside its own screens.

| keys | where | what | project |
|---|---|---|---|
| shift + C# | any screen | starts or stops all sequencer slots (euclid, dots; oracle and peal too) | op1r |
| shift + F, G, A, B (the first four white keys) | any screen | pattern 1-4 | op1r |
| shift + G, A, B, C, D, E (the last six white keys) | any screen | mutes sequencer slots 1-6 | op1r |
| shift + D# | any screen | mutes all sequencer slots | op1r |
| T1 | the clock screen (shift + help) | resource monitor | op1r |
| T2 | the clock screen (shift + help) | USB out page (blue: master, or master + the four tape tracks; green: MIDI SEQ on / off, since op1r 35) | op1r |
| T3 | the clock screen (shift + help) | settings page: the count-in's length (since op1r 22) | op1r |
| orange encoder press (op1r calls it red) | the tape screen | sets a tape marker | op1r |
| shift + orange encoder press | the tape screen | removes the marker under the cursor; the same press as Oblique Strategies' card | op1r |
| shift + orange encoder turn | the tape screen | jumps to the next / previous marker (stock: the record level) | op1r |
| shift + press the orange encoder | any screen | shows a random Oblique Strategies card; while it shows, any key closes it and that press does nothing else. On top of op1r it runs before op1r's key handling, so it would take op1r's shift + red on the dots and euclid screens if that means the red encoder press (not checked) | Oblique Strategies |
| shift + help | the clock screen | shows a random Oblique Strategies card in the clock's place; again switches card / clock (since op1r 21; stock: does nothing there). The standalone Oblique Strategies mod uses shift + orange encoder press instead | op1r |
| hold a note key (shift + key latches) | any screen, while oracle or peal is the sequencer | oracle plays transposed to the key; peal rings the held keys (3–8) as bells, like the stock sequencers | op1r |
| hold REC + metronome | any screen, the tape stopped | count-in (4 / 8 / 16 clicks), then recording starts; again cancels (since op1r 22) | op1r |
| hold tape + REC | any screen | arms punch in / out at the tape markers; again cancels (since op1r 23) | op1r |
| hold synth + scissors | the sampler page | the sample editor (since op1r 24) | op1r |
| hold drum + scissors | the drum page | the drum sample editor (since op1r 25) | op1r |
| sequencer + tape | any screen, with MIDI SEQ on (clock screen, T2) | op1r's 4-track MIDI sequencer; with MIDI SEQ off it does what stock does (since op1r 35) | op1r |
| synth + drum + tape + mixer, held together | any screen | Opus's menu (stock: the helicopter game) | Opus |
| help | any screen | Opus's FN: a modifier for plugins' controls (stock: the help overlay, gone; shift + help's date and time is in Opus's menu, system) | Opus |
| tape + left / tape + right | the tape screen | tape undo / redo (opus.tapeundo) | Opus |
| shift + left / shift + right | the tape screen, the loop playing, with tape undo's "loop lock" on (off by default) | the loop no longer jumps by its own length, as stock queues it (opus.tapeundo) | Opus |
| shift + left / shift + right | where stock bends: the synth and drum screens, COM, the preset browser | pitch bend down / up, its depth, speed and curve set (opus.bend) | Opus |
| hold synth or drum + s1-s8 through the save clock | any screen | overwrite save (opus.overwrite) | Opus |
| push blue / push green | the synth's T1 page | the scales / chords quick pages (opus.scales) | Opus |
| shift + push white / shift + push orange | the synth's pages | dice: a random sound / undo the last roll (opus.dice; shift + orange press is also Oblique Strategies' card) | Opus |
| push white / push orange; white / orange turn | the synth's shift page (synth, T2, hold shift) | pitch bend: up / down depth; curve / speed (opus.bend) | Opus |
| shift + white turn | the tape screen | zooms the tape view (opus.zoom; plain white still sets the tape's speed) | Opus |
| push orange | the preset browser (shift + s1-s8), on your own presets | rename (opus.rename) | Opus |
| play / stop | any screen, while the tape plays ("play as pause", on by default) | play pauses; stop jumps back and plays on (opus.playpause) | Opus |
| green turn | the effect list (shift + T3) | chooses the second effect (opus.overdrive) | Opus |
| push blue | an effect's page (T3 on the synth, drum or mixer) | the first or the second effect's page (opus.overdrive) | Opus |

### MIDI

CC numbers and SysEx messages a mod answers to.

| message | what | project |
|---|---|---|
| CC 5-52 | the keys, as in the OP-1's own CTRL mode (key code + 5) | op1r |
| CC 102-105 | the four encoders, relative | op1r |
| CC 106-118 | mixer volume, pan and mute per track, tape input | op1r |
| CC 53-60, 72-79 | synth automation of the current synth slot, absolute: 53-56 engine knobs, 57-60 envelope A/D/S/R, 72-75 FX knobs, 76-79 LFO knobs (since op1r 35) | op1r |
| SysEx F0 00 20 76 00 01 03 F7 / ... 00 F7 | OP-Z controller mode on / off | op1r |
| SysEx F0 00 20 76 7D <cmd> ... F7 | firmware and plugin update over USB: files are staged, the OP-1 asks before applying them (since op1r 31; 00 20 76 is Teenage Engineering's maker ID) | op1r |
| a second USB MIDI port | the dev port; in the release it answers ping and version, and memory reads while the developer mode is on (Opus's menu, system) | Opus |

### Files and folders

Files a mod adds to the update package, and files and folders it writes on the OP-1.

| path | project |
|---|---|
| content/display/dots.svg, euclid.svg, fxgeneric.svg, iterlab.svg, oracle.svg, peal.svg, quadlfo.svg, sysmon.svg, usbout.svg (the plugins' screens are inside their files) | op1r |
| plugins/<name>.op1p in the update package; on the OP-1 /yaffs2/plugins/<name>.op1p and /yaffs2/plugins/.boot (a crash marker: found at start-up, all plugin files are skipped once) | op1r |
| /yaffs2/op1r_stage/ (updates over USB, staged until applied) | op1r |
| /yaffs2/user/op1r_seq.mseq (the MIDI sequencer's song) | op1r |
| op1.db: the table op1rplugins (plugin files' numbers) | op1r |
| content/opus.txt (added: marks an Opus install) | Opus |
| /yaffs2/mod/ (settings.a, settings.b; mods/, the plugin files, shown on the USB disk as /mods; a folder per plugin ID with its settings and files, some shown as /mods/NAME; themes/, splash/, skip/, crash/; the cleaner's clean and cleaned; journals) | Opus |
| /yaffs2/mod/opus.tapeundo/undo0.tmp, undo1.tmp, undo2.tmp (Opus 1's /yaffs2/user/tapeundo*.tmp deleted at start) | Opus |
| op1.db: the table opus_kept (the cleaner's copies) | Opus |

### Changes to the firmware files

Where a mod changes the files in the update package. Two mods that change the same bytes can't go in one build.

| file | change | project |
|---|---|---|
| OP1_vdk.ldr | 86 replaced ranges and a 181,708-byte block inserted at offset 2,171,351, among them the CALL at 0x019F02EE (Clips::load: the plugin loader); the full list is in data/manifest.json | op1r |
| content/op1_factory.db | 15 edits: the fixed rows above (filter, iter, drum+, the sequencers); the plugins' rows are added at start-up | op1r |
| OP1_vdk.ldr | CALLs at 0x019C2D3E (key handler, also patched by op1r: it chains to whatever is there) and 0x01A3BC0E (end of the GUI frame) redirected; an 8,360-byte block inserted before the FINAL block; the FIRST block's length and checksum | Oblique Strategies |
| OP1_vdk.ldr | 129 changed ranges (248 bytes) in 15 of the OS's blocks, among them the key handler's CALLs at 0x019C2D3E (also redirected by op1r and Oblique Strategies) and 0x019C2E94; a 190,052-byte block loaded at 0x01E00000 and a zero-filled block after it | Opus |
| the OS's code in RAM, at start | each loaded plugin's places (its manifest's place lines: the address and the stock bytes it expects); a place whose bytes differ, or that another plugin holds, is refused and the plugin not loaded | Opus |

### Memory

RAM a mod's code and data use while the OP-1 runs.

| range | what | project |
|---|---|---|
| 0x01E00000-0x01E2C574 | code and data (one LDR block, op1r 35; it stays below 0x01E40000) | op1r |
| 0x01E40000-0x01E420A8 | code, card text and state (one LDR block) | Oblique Strategies |
| 0x01EC0000-0x01EEA0CC | zeroed data (an LDR fill block, op1r 35) | op1r |
| 0xFFA0BFB4-0xFFA0BFDC | 40 bytes in L1 instruction memory (an LDR block) | op1r |
| the heap (malloc) | plugin files' code and data, loaded at start-up | op1r |
| 0x01E00000-0x01E2E664 | code and data (one LDR block) | Opus |
| 0x01E2E664-0x01E5698C | zeroed state (a FILL block) | Opus |
| 0x01E569A0-0x01F00000 | the plugins' near pool: their code and data, within a call's reach of the OS's code | Opus |
| 0x01F00000-0x01F32000 | the menu's page cache | Opus |
| 0x01F40000-0x01F5E000 | colours' tables | Opus |
| 0x01FA0000-0x01FBE420 | the core's large buffers, cleared at start-up | Opus |
| 0x02C00000-0x02FFE000 | the plugins' far pool | Opus |
| 0x02FFE000-0x03000000 | the crash record, kept through a restart | Opus |
| 0x03000000-0x03032000 | the start-up picture (opus.splash), built in the OS's second frame buffer before the OS uses it | Opus |
| 0xFF90081C-0xFF906908, 0xFF907E00-0xFF908000 | the plugins' fast memory (L1 data): the helicopter game's sounds, silenced (the game can't be reached), and 512 free bytes | Opus |

### Version text

What a build calls itself, so bug reports and tools can tell builds apart.

| project | version string | shown |
|---|---|---|
| stock 246 | R. 00246 |  |
| op1r |  op1r 35 (in place of R. 00246) | the boot screen shows op1r and its version under the TE logo |
| Oblique Strategies | unchanged |  |
| Opus | unchanged (R. 00246) | Opus's menu: hold help on its main page for "opus 2" and "build 1"; the diagnostics (T3), system tab: "2 build 1"; the dev port's version command |

### Names a firmware doesn't know

What a firmware does with a sound that names an effect or engine it doesn't have.

| firmware | unknown effect | unknown engine |
|---|---|---|
| stock 246 | crashes ([op-forums #945](https://op-forums.com/t/4283/945)) | locks up with "patch.cpp:390 Invalid synth patch" (op1r's changelog, op1r 18) |
| op1r | loads the sound with the filter (since op1r 34; before, an unknown name stopped the OP-1 at boot, as on stock); an effect number with no plugin plays the filter | loads the sound as iter (since op1r 18); an engine number with no plugin plays iter |
| Opus | plays it as cwo, switched off; the sound itself is never rewritten. A second effect (Fx overdrive) of a type it doesn't know plays nothing and is written back as it was | in a slot at start, plays a stand-in (the first cluster preset); the browser refuses it and says which plugin it needs ("needs opus.dx"); the sound is never rewritten. An iter sound with a mark (knobs[4] 0x100 or more) no loaded plugin has counts as unknown; below 0x100 it plays as the OS's iter |

### How each was checked

- stock 246: content/op1_factory.db in op1_246.op1 (SHA-256 c5315218f825f143b415ca554516541898abee843d3a236df0b54c04e1fb13a9)
- op1r: data/manifest.json (its op1_factory.db edits applied to stock) and its inserted LDR block, op1r 35 (output SHA-256 061d85652ed1892a57ed37c4d0e6b4d85f348d73700ccd07879d60d6b5788d55, all plugins), README.md, CHANGELOG.md; op1r-src synth_sdk/plugins/ORDERS.md, op1_plugin.h, plugload/plugload.c, devupd/du.h
- Opus: its update file op1_246_opus2.op1 (SHA-256 42d63d5d07319f0dcf7795b493c20dc3e57c41463b680cf3a22a1ca11b04f26e), its starter pack opus2-starter-pack.zip (SHA-256 9dfdca508784a07875857c850d57ce21dd4d46843b70fee230750e0845aa6b63), bridge.opmod (SHA-256 07f1e1f5407cfc5fc38304c6df36f896f50f3aa9c3e7c77b9ce9fee796ea1582) and their source; the rows of op1_factory.db read back in the emulator with the whole pack
- Oblique Strategies: patch_oblique.py and README.md (patch list, hook sites); stock output SHA-256 e452aa9576ec8af500442d95bc373eaf2ed9a3634cf5c972c73908067a7ed1db
- Squarewave Studio: the author's own entry (issue #2, 2026-10-13); not released yet

<!-- tables:end -->

## Proposed conventions

_A proposal: open an issue to discuss it._

1. **A name means one thing.** Lowercase and short, and not used by stock or another mod for
   something else. Mods that unlock the same stock thing (like the hidden filter) use the same name.
2. **Don't crash on names you don't know.** Play something safe instead and keep the original name
   when the sound is saved, so sounds can move between firmwares.
3. **Rows, for combined builds.** A new project takes a block of 16 rows per table from 32 up
   (32-47, 48-63, ...) and notes it here. Rows that have already shipped stay as they are.
4. **Engines in iter's slot:** record where your marker goes and its values.
5. **Name your build in its version text**, so a bug report says which firmware it was.
6. **Record what you take:** key combinations, MIDI messages, files, firmware bytes and memory.

## Add or correct an entry

- Edit `registry.json`, run `python tools/check.py --write` to update the tables here, and open a
  pull request. The same check runs on every pull request.
- Or open an issue with the form, and it gets added for you.
- A mod that isn't released yet can record its entries early, to claim them.

## Not affiliated

There is no firmware in this repository. It is not affiliated with or endorsed by Teenage
Engineering; OP-1 is a trademark of Teenage Engineering AB. The list is public domain (CC0), so any
tool can use it.
