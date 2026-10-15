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
| [Opus](https://opus-op1.pages.dev) | LizardMan | 1.0.1 (build 90) | adds its effect rows by name when the OP-1 starts (the next free rows), so it holds no fixed row numbers; its engines run in iter's slot |
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
| filter | - | Opus | the same hidden filter as op1r's; row added at start-up (11 on a stock database) |
| bitcrush | - | Opus | row added at start-up (12 on a stock database) |
| chorus | - | Opus | row added at start-up (13 on a stock database) |
| plate | - | Opus | a reverb; row added at start-up (14 on a stock database) |

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
| iter | - | Opus | not in Opus's engine list: Opus's own engines run in its slot. At start Opus deletes a row 11 named iter (its own builds 29-57 added it; op1r uses that row too) |
| dimension | - | Opus | runs in iter's slot: marker 0x4F01 |
| amp | - | Opus | guitar amp; runs in iter's slot: marker 0x4F02 |

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
| opus | Opus's member: "v" and "uses" (the Opus parts a sound needs, by plugin ID, e.g. "opus.dimension": 1), and the second effect: fx2_type (by name), fx2_active, fx2_params | Opus |

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
| tape + left / tape + right | any screen | tape undo / redo | Opus |
| shift + left / shift + right | any screen | pitch bend down / up | Opus |
| hold synth or drum + s1-s8 through the save clock | any screen | overwrite save | Opus |
| push blue / push green | a synth engine's T1 screen | the scales / chords quick menu | Opus |
| shift + push white / shift + push orange | the synth's pages | dice: a random sound / undo (shift + orange press is also Oblique Strategies' card) | Opus |
| push white / push orange; white / orange turn | the synth's shift page (synth, T2, hold shift) | pitch bend: up / down depth; curve / speed | Opus |
| shift + white turn | the tape screen | zooms the tape view (plain white still sets the tape's speed) | Opus |
| push orange | the preset browser (shift + s1-s8), on your own presets | rename | Opus |
| play / stop | the tape, with "play pause" on in Opus's menu | play pauses; stop jumps back and plays on | Opus |
| green | the effect list (shift + T3), with fx overdrive on | chooses the second effect | Opus |
| push blue; T3 | an effect page, with fx overdrive on | switches between the two effects' screens; the second effect on / off | Opus |

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
| a second USB MIDI port | the dev port; in the release it answers ping and version only | Opus |

### Files and folders

Files a mod adds to the update package, and files and folders it writes on the OP-1.

| path | project |
|---|---|
| content/display/dots.svg, euclid.svg, fxgeneric.svg, iterlab.svg, oracle.svg, peal.svg, quadlfo.svg, sysmon.svg, usbout.svg (the plugins' screens are inside their files) | op1r |
| plugins/<name>.op1p in the update package; on the OP-1 /yaffs2/plugins/<name>.op1p and /yaffs2/plugins/.boot (a crash marker: found at start-up, all plugin files are skipped once) | op1r |
| /yaffs2/op1r_stage/ (updates over USB, staged until applied) | op1r |
| /yaffs2/user/op1r_seq.mseq (the MIDI sequencer's song) | op1r |
| op1.db: the table op1rplugins (plugin files' numbers) | op1r |
| content/opus.txt (added: marks an Opus install), content/display/save.svg (replaced: the save overlay with "overwriting") | Opus |
| /yaffs2/mod/ (settings.a, settings.b, clean, cleaned, themes/, splash/; the USB disk shows /themes and /splash) | Opus |
| /yaffs2/user/tapeundo0.tmp, tapeundo1.tmp, tapeundo2.tmp | Opus |
| op1.db: the table opus_kept (the cleaner's copies) | Opus |

### Changes to the firmware files

Where a mod changes the files in the update package. Two mods that change the same bytes can't go in one build.

| file | change | project |
|---|---|---|
| OP1_vdk.ldr | 86 replaced ranges and a 181,708-byte block inserted at offset 2,171,351, among them the CALL at 0x019F02EE (Clips::load: the plugin loader); the full list is in data/manifest.json | op1r |
| content/op1_factory.db | 15 edits: the fixed rows above (filter, iter, drum+, the sequencers); the plugins' rows are added at start-up | op1r |
| OP1_vdk.ldr | CALLs at 0x019C2D3E (key handler, also patched by op1r: it chains to whatever is there) and 0x01A3BC0E (end of the GUI frame) redirected; an 8,360-byte block inserted before the FINAL block; the FIRST block's length and checksum | Oblique Strategies |
| OP1_vdk.ldr | 222 changed ranges (838 bytes) in 17 of the OS's blocks, among them the key handler's CALL at 0x019C2D3E (also redirected by op1r and Oblique Strategies); a 284,556-byte block loaded at 0x01E00000 and a zero-filled block after it | Opus |
| content/display/save.svg | replaced (overwrite save's screen) | Opus |

### Memory

RAM a mod's code and data use while the OP-1 runs.

| range | what | project |
|---|---|---|
| 0x01E00000-0x01E2C574 | code and data (one LDR block, op1r 35; it stays below 0x01E40000) | op1r |
| 0x01E40000-0x01E420A8 | code, card text and state (one LDR block) | Oblique Strategies |
| 0x01EC0000-0x01EEA0CC | zeroed data (an LDR fill block, op1r 35) | op1r |
| 0xFFA0BFB4-0xFFA0BFDC | 40 bytes in L1 instruction memory (an LDR block) | op1r |
| the heap (malloc) | plugin files' code and data, loaded at start-up | op1r |
| 0x01E00000-0x01E4578C | code and data (one LDR block) | Opus |
| 0x01E4578C-0x01EF3228 | zeroed state (a FILL block) | Opus |
| 0x01F00000-0x01F40000 | the menu's page cache | Opus |
| 0x01F40000-0x01F5E000 | colours' tables | Opus |
| 0x01F60000-0x01FA0000 | the plate's second-effect tanks | Opus |
| 0x01FA0000-0x02000000 | large buffers, cleared at start-up | Opus |

### Version text

What a build calls itself, so bug reports and tools can tell builds apart.

| project | version string | shown |
|---|---|---|
| stock 246 | R. 00246 |  |
| op1r |  op1r 35 (in place of R. 00246) | the boot screen shows op1r and its version under the TE logo |
| Oblique Strategies | unchanged |  |
| Opus | unchanged (R. 00246) | Opus's menu: hold help for "opus 1" and the build |

### Names a firmware doesn't know

What a firmware does with a sound that names an effect or engine it doesn't have.

| firmware | unknown effect | unknown engine |
|---|---|---|
| stock 246 | crashes ([op-forums #945](https://op-forums.com/t/4283/945)) | locks up with "patch.cpp:390 Invalid synth patch" (op1r's changelog, op1r 18) |
| op1r | loads the sound with the filter (since op1r 34; before, an unknown name stopped the OP-1 at boot, as on stock); an effect number with no plugin plays the filter | loads the sound as iter (since op1r 18); an engine number with no plugin plays iter |
| Opus | plays it as cwo, switched off; the sound itself is never rewritten | plays a stand-in (the first cluster preset) and the browser says "incompatible preset"; the sound is never rewritten. An iter sound without one of Opus's markers counts as unknown |

### How each was checked

- stock 246: content/op1_factory.db in op1_246.op1 (SHA-256 c5315218f825f143b415ca554516541898abee843d3a236df0b54c04e1fb13a9)
- op1r: data/manifest.json (its op1_factory.db edits applied to stock) and its inserted LDR block, op1r 35 (output SHA-256 061d85652ed1892a57ed37c4d0e6b4d85f348d73700ccd07879d60d6b5788d55, all plugins), README.md, CHANGELOG.md; op1r-src synth_sdk/plugins/ORDERS.md, op1_plugin.h, plugload/plugload.c, devupd/du.h
- Opus: its update file op1_246_opus.op1 (SHA-256 b4e37fc48fecbb83d71923bc34c209bf7cc4b7658f0c24b4b33888199f7adbc2) and its source
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
