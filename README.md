# OP-1 mod registry

Which names and numbers each mod for the original OP-1 (firmware 246) adds, so mods, and the sounds
made with them, don't clash.

The list is [`registry.json`](registry.json); the tables below are made from it. If you make a mod
for 246, add yours: see [Add or correct an entry](#add-or-correct-an-entry).

## Why it matters

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
| [op1r](https://github.com/pcppcp/op1r) | popcorp | op1r 18 (fb06689) |  |
| [#249](https://maikopruett.com/op-1) | maiko | #249 (2026-10-11) | carries op1r's synths, effects and sequencers with op1r 18's names and rows, so it has no rows of its own here |
| Opus | LizardMan | in development | its entries come before its first release |

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

### Engines hosted in iter's slot

A mod can run its engines in the slot of iter, stock's hidden engine. Their sounds then say `"type": "iter"`, so each mod marks which engine a sound is for. Record where the mark goes and its values, so two mods don't use the same one.

_Nothing recorded yet._

### Drum engines (`drum_types`)

| name | row | project | note |
|---|---|---|---|
| dbox | 1 | stock 246 |  |

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

### Keys added inside sound files

Sounds are JSON. Record any key a mod adds, so two mods don't use one key for different things.

_Nothing recorded yet._

### Key combinations

Combinations a mod takes outside its own screens.

| keys | where | what | project |
|---|---|---|---|
| shift + C# | any screen | starts or stops all sequencer slots | op1r |
| shift + F, G, A, B (the first four white keys) | any screen | pattern 1-4 | op1r |
| shift + G, A, B, C, D, E (the last six white keys) | any screen | mutes sequencer slots 1-6 | op1r |
| shift + D# | any screen | mutes all sequencer slots | op1r |
| T1 | the clock screen (shift + help) | resource monitor | op1r |

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
| content/display/cloudsfx.svg, dots.svg, euclid.svg, fmbell.svg, fxgeneric.svg, granular.svg, iterlab.svg, kalireverb.svg, quadlfo.svg, supersaw.svg, sysmon.svg, tapeecho.svg | op1r |

### Changes to the firmware files

Where a mod changes the files in the update package. Two mods that change the same bytes can't go in one build.

| file | change | project |
|---|---|---|
| OP1_vdk.ldr | 52 replaced ranges and a 204,928-byte block inserted at offset 2,171,347; the full list is in data/manifest.json | op1r |
| content/op1_factory.db | 14 edits (the rows above) | op1r |

### Memory

RAM a mod's code and data use while the OP-1 runs.

_Nothing recorded yet._

### Version text

What a build calls itself, so bug reports and tools can tell builds apart.

| project | version string | shown |
|---|---|---|
| stock 246 | R. 00246 |  |
| op1r |  op1r 18 (in place of R. 00246) | the boot screen shows op1r and its version under the TE logo |

### Names a firmware doesn't know

What a firmware does with a sound that names an effect or engine it doesn't have.

| firmware | unknown effect | unknown engine |
|---|---|---|
| stock 246 | crashes ([op-forums #945](https://op-forums.com/t/4283/945)) | locks up with "patch.cpp:390 Invalid synth patch" (op1r's changelog, op1r 18) |
| op1r | not documented | loads the sound as iter (since op1r 18) |

### How each was checked

- stock 246: content/op1_factory.db in op1_246.op1 (SHA-256 c5315218f825f143b415ca554516541898abee843d3a236df0b54c04e1fb13a9)
- op1r: data/manifest.json (its op1_factory.db edits applied to stock), README.md, CHANGELOG.md
- #249: content/op1_factory.db in op1_249.op1 (SHA-256 b7adf5c0fdd523a726e81880e683eda48061a261944dfa1a7a52c57ebfc41066)

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
