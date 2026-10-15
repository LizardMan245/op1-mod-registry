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
| [op1r](https://github.com/pcppcp/op1r) | popcorp | op1r 31 (380a0af) |  |
| Opus | LizardMan | in development | its entries come before its first release |
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
| tape | 11 | op1r | tape echo |
| clouds | 12 | op1r |  |
| reverb | 13 | op1r | its screen says "Kali" |
| palme | 14 | op1r | Musica Obscura by ultralazr; Ondes Martenot diffuseur |
| in a room | 15 | op1r | Musica Obscura by ultralazr; Lucier's I am sitting in a room. Sounds saved as "sitting" (test builds) load as it |

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
| supersaw | 12 | op1r |  |
| fmbell | 13 | op1r |  |
| granular | 14 | op1r |  |
| strata | - | Squarewave Studio | in development |
| mixtur | 15 | op1r | Musica Obscura by ultralazr; Mixtur-Trautonium undertones |
| arc | 16 | op1r | Musica Obscura by ultralazr; Duddell's singing arc |

### Engines hosted in iter's slot

A mod can run its engines in the slot of iter, stock's hidden engine. Their sounds then say `"type": "iter"`, so each mod marks which engine a sound is for. Record where the mark goes and its values, so two mods don't use the same one.

| marker | where | engine | project |
|---|---|---|---|
| synth 21249 (0x5300 + 1) | knobs[4] of a sound with "type": "iter" | supersaw | op1r |
| synth 21250 (0x5300 + 2) | knobs[4] of a sound with "type": "iter" | fmbell | op1r |
| synth 21251 (0x5300 + 3) | knobs[4] of a sound with "type": "iter" | granular | op1r |
| synth 21256 (0x5300 + 8) | knobs[4] of a sound with "type": "iter" | mixtur | op1r |
| synth 21257 (0x5300 + 9) | knobs[4] of a sound with "type": "iter" | arc | op1r |
| FX 21249 (0x5300 + 1) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | tape | op1r |
| FX 21250 (0x5300 + 2) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | clouds | op1r |
| FX 21251 (0x5300 + 3) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | reverb | op1r |
| FX 21254 (0x5300 + 6) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | palme | op1r |
| FX 21255 (0x5300 + 7) | knobs[4] of an effect with "fx_type": "filter" (op1r runs its FX in the filter slot) | in a room | op1r |
| 0x5300 + 4 … 7 (synth), 0x5300 + 4, 5 (FX) | reserved in op1r-src plugins/ORDERS.md | Hundekraft's workshop engines and effects (wavetable, taffy, pew, elg; washer, snowglobe) | op1r |

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

_Nothing recorded yet._

### Key combinations

Combinations a mod takes outside its own screens.

| keys | where | what | project |
|---|---|---|---|
| shift + C# | any screen | starts or stops all sequencer slots (euclid, dots; oracle and peal too) | op1r |
| shift + F, G, A, B (the first four white keys) | any screen | pattern 1-4 | op1r |
| shift + G, A, B, C, D, E (the last six white keys) | any screen | mutes sequencer slots 1-6 | op1r |
| shift + D# | any screen | mutes all sequencer slots | op1r |
| T1 | the clock screen (shift + help) | resource monitor | op1r |
| T2 | the clock screen (shift + help) | USB out page (master, or master + the four tape tracks) | op1r |
| orange encoder press (op1r calls it red) | the tape screen | sets a tape marker | op1r |
| shift + orange encoder press | the tape screen | removes the marker under the cursor; the same press as Oblique Strategies' card | op1r |
| shift + orange encoder turn | the tape screen | jumps to the next / previous marker (stock: the record level) | op1r |
| shift + press the orange encoder | any screen | shows a random Oblique Strategies card; while it shows, any key closes it and that press does nothing else. On top of op1r it runs before op1r's key handling, so it would take op1r's shift + red on the dots and euclid screens if that means the red encoder press (not checked) | Oblique Strategies |
| shift + help | any screen (the clock screen) | shows a random Oblique Strategies card in the clock's place; shift + help again switches card / clock (since op1r 21). The standalone Oblique Strategies mod uses shift + orange encoder press instead | op1r |
| hold a note key (shift + key latches) | any screen, while oracle or peal is the sequencer | oracle plays transposed to the key; peal rings the held keys (3–8) as bells, like the stock sequencers | op1r |

### MIDI

CC numbers and SysEx messages a mod answers to.

| message | what | project |
|---|---|---|
| CC 5-52 | the keys, as in the OP-1's own CTRL mode (key code + 5) | op1r |
| CC 102-105 | the four encoders, relative | op1r |
| CC 106-118 | mixer volume, pan and mute per track, tape input | op1r |
| SysEx F0 00 20 76 00 01 03 F7 / ... 00 F7 | OP-Z controller mode on / off | op1r |

### Files and folders

Files a mod adds to the update package, and files and folders it writes on the OP-1.

| path | project |
|---|---|
| content/display/cloudsfx.svg, dots.svg, duddell.svg, euclid.svg, fmbell.svg, fxgeneric.svg, granular.svg, iterlab.svg, kalireverb.svg, lucierroom.svg, mixtur.svg, oracle.svg, palmediff.svg, peal.svg, quadlfo.svg, supersaw.svg, sysmon.svg, tapeecho.svg, usbout.svg | op1r |

### Changes to the firmware files

Where a mod changes the files in the update package. Two mods that change the same bytes can't go in one build.

| file | change | project |
|---|---|---|
| OP1_vdk.ldr | 76 replaced ranges and a 251,652-byte block inserted at offset 2,171,351; the full list is in data/manifest.json | op1r |
| content/op1_factory.db | 16 edits (the rows above) | op1r |
| OP1_vdk.ldr | CALLs at 0x019C2D3E (key handler, also patched by op1r: it chains to whatever is there) and 0x01A3BC0E (end of the GUI frame) redirected; an 8,360-byte block inserted before the FINAL block; the FIRST block's length and checksum | Oblique Strategies |

### Memory

RAM a mod's code and data use while the OP-1 runs.

| range | what | project |
|---|---|---|
| 0x01E00000-0x01E3D6AC | code and data (one LDR block, op1r 31; it stays below 0x01E40000) | op1r |
| 0x01E40000-0x01E420A8 | code, card text and state (one LDR block) | Oblique Strategies |
| 0x01EC0000-0x01EECEA4 | zeroed data (an LDR fill block, op1r 31) | op1r |

### Version text

What a build calls itself, so bug reports and tools can tell builds apart.

| project | version string | shown |
|---|---|---|
| stock 246 | R. 00246 |  |
| op1r |  op1r 31 (in place of R. 00246) | the boot screen shows op1r and its version under the TE logo |
| Oblique Strategies | unchanged |  |

### Names a firmware doesn't know

What a firmware does with a sound that names an effect or engine it doesn't have.

| firmware | unknown effect | unknown engine |
|---|---|---|
| stock 246 | crashes ([op-forums #945](https://op-forums.com/t/4283/945)) | locks up with "patch.cpp:390 Invalid synth patch" (op1r's changelog, op1r 18) |
| op1r | an unknown name stops the OP-1 at boot, as on stock (fx_types.cpp:42); an op1r effect number with no plugin in the build plays the filter | loads the sound as iter (since op1r 18); an engine number with no plugin plays iter |

### How each was checked

- stock 246: content/op1_factory.db in op1_246.op1 (SHA-256 c5315218f825f143b415ca554516541898abee843d3a236df0b54c04e1fb13a9)
- op1r: data/manifest.json and the patched op1_factory.db of op1r 31 (output SHA-256 b79949491d19ec803d71f9e76d154689556669d4af8f000ec96d39834484e180), README.md, CHANGELOG.md, op1r-src plugins/ORDERS.md
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
