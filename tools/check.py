"""Checks registry.json and keeps the tables in README.md in step with it.

    python tools/check.py            check; fails when README.md's tables are out of date
    python tools/check.py --write    check, then rewrite README.md's tables
"""
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
START, END = "<!-- tables:start -->", "<!-- tables:end -->"

# (key, title, one line on what it is); named tables have name, row, project, note
NAMED = {
    "fx_types": ("Effects (`fx_types`)", "Sounds store the effect's name. The row is its row in `content/op1_factory.db`."),
    "synth_types": ("Synth engines (`synth_types`)", "Sounds store the engine's name as `type`."),
    "drum_types": ("Drum engines (`drum_types`)", ""),
    "lfo_types": ("LFOs (`lfo_types`)", ""),
    "seq_types": ("Sequencers (`seq_types`)", ""),
}
# (key, title, one line, [(column label, field)])
LISTS = {
    "iter_markers": ("Engines hosted in iter's slot",
                     "A mod can run its engines in the slot of iter, stock's hidden engine. Their sounds then say "
                     "`\"type\": \"iter\"`, so each mod marks which engine a sound is for. Record where the mark "
                     "goes and its values, so two mods don't use the same one.",
                     [("marker", "marker"), ("where", "where"), ("engine", "name"), ("project", "project")]),
    "sound_keys": ("Keys added inside sound files",
                   "Sounds are JSON. Record any key a mod adds, so two mods don't use one key for different things.",
                   [("key", "key"), ("what", "what"), ("project", "project")]),
    "keys": ("Key combinations", "Combinations a mod takes outside its own screens.",
             [("keys", "keys"), ("where", "where"), ("what", "what"), ("project", "project")]),
    "midi": ("MIDI", "CC numbers and SysEx messages a mod answers to.",
             [("message", "message"), ("what", "what"), ("project", "project")]),
    "files": ("Files and folders",
              "Files a mod adds to the update package, and files and folders it writes on the OP-1.",
              [("path", "path"), ("project", "project")]),
    "firmware_patches": ("Changes to the firmware files",
                         "Where a mod changes the files in the update package. Two mods that change the same "
                         "bytes can't go in one build.",
                         [("file", "file"), ("change", "change"), ("project", "project")]),
    "memory": ("Memory", "RAM a mod's code and data use while the OP-1 runs.",
               [("range", "range"), ("what", "what"), ("project", "project")]),
    "build_id": ("Version text", "What a build calls itself, so bug reports and tools can tell builds apart.",
                 [("project", "project"), ("version string", "version_string"), ("shown", "shown")]),
    "unknown_names": ("Names a firmware doesn't know",
                      "What a firmware does with a sound that names an effect or engine it doesn't have.",
                      [("firmware", "project"), ("unknown effect", "effect"), ("unknown engine", "engine")]),
}
ORDER = ["fx_types", "synth_types", "iter_markers", "drum_types", "lfo_types", "seq_types", "sound_keys",
         "keys", "midi", "files", "firmware_patches", "memory", "build_id", "unknown_names"]


def rows_of(r):
    return [] if r is None else r if isinstance(r, list) else [r]


def check(reg):
    errors, warnings = [], []
    projects = reg.get("projects", {})
    for key in ORDER:
        if not isinstance(reg.get(key), list):
            errors.append(f"{key}: missing or not a list")
    for key in ORDER:
        for i, e in enumerate(reg.get(key) or []):
            if e.get("project") not in projects:
                errors.append(f"{key}[{i}]: unknown project {e.get('project')!r}")
    for key in NAMED:
        seen = {}
        for e in reg.get(key) or []:
            name, r = e.get("name", ""), e.get("row")
            if not re.fullmatch(r"[a-z0-9_]+", name):
                errors.append(f"{key}: name {name!r}: use lowercase letters, digits and _")
            if not (r is None or isinstance(r, int) or (isinstance(r, list) and r and all(isinstance(x, int) for x in r))):
                errors.append(f"{key} {name}: row must be a number, a list of numbers or null")
            for other in seen.get(name, []):
                if other["project"] != e["project"] and e.get("same_as") != other["project"] and other.get("same_as") != e["project"]:
                    errors.append(f"{key}: {name!r} is used by {other['project']} and {e['project']}; "
                                  f"if it's the same thing, add \"same_as\"")
            seen.setdefault(name, []).append(e)
        claimed = {}
        for e in reg.get(key) or []:
            for r in rows_of(e.get("row")):
                for p in claimed.get(r, set()) - {e["project"]}:
                    warnings.append(f"{key}: row {r} is used by {p} and {e['project']} (only matters in a combined build)")
                claimed.setdefault(r, set()).add(e["project"])
    for key, field in (("iter_markers", "marker"), ("sound_keys", "key")):
        values = [str(e.get(field)) for e in reg.get(key) or []]
        for v in sorted({v for v in values if values.count(v) > 1}):
            errors.append(f"{key}: {v} is listed twice")
    return errors, sorted(set(warnings))


def cell(v):
    if isinstance(v, list):
        v = f"{v[0]}-{v[-1]}" if v == list(range(v[0], v[-1] + 1)) and len(v) > 1 else ", ".join(map(str, v))
    return ("" if v is None else str(v)).replace("|", "\\|").replace("\n", " ")


def tables(reg):
    name = {k: p["name"] for k, p in reg["projects"].items()}
    out = ["### Projects", "", "| project | by | version | note |", "|---|---|---|---|"]
    for p in reg["projects"].values():
        title = f"[{cell(p['name'])}]({p['url']})" if p.get("url") else cell(p["name"])
        out.append(f"| {title} | {cell(p.get('by'))} | {cell(p.get('version'))} | {cell(p.get('note'))} |")
    out.append("")
    for key in ORDER:
        if key in NAMED:
            title, line = NAMED[key]
            cols = [("name", "name"), ("row", "row"), ("project", "project"), ("note", "note")]
        else:
            title, line, cols = LISTS[key]
        out += [f"### {title}", ""] + ([line, ""] if line else [])
        entries = reg.get(key) or []
        if not entries:
            out += ["_Nothing recorded yet._", ""]
            continue
        out.append("| " + " | ".join(c for c, _ in cols) + " |")
        out.append("|" + "---|" * len(cols))
        for e in entries:
            vals = []
            for _, f in cols:
                v = e.get(f)
                if f == "project":
                    v = name.get(v, v)
                elif f == "row" and v is None:
                    v = "none"
                elif f == "row" and isinstance(v, list):  # rows that depend on the build's options
                    v = " or ".join(map(str, v)) if len(v) == 2 else f"one of {v[0]}-{v[-1]}"
                vals.append(cell(v))
            out.append("| " + " | ".join(vals) + " |")
        out.append("")
    out += ["### How each was checked", ""]
    out += [f"- {cell(p['name'])}: {cell(p['checked'])}" for p in reg["projects"].values() if p.get("checked")]
    return "\n".join(out).rstrip("\n")


def main():
    reg = json.load(open(os.path.join(ROOT, "registry.json"), encoding="utf-8"))
    errors, warnings = check(reg)
    for w in warnings:
        print("note:", w)
    for e in errors:
        print("error:", e)
    path = os.path.join(ROOT, "README.md")
    readme = open(path, encoding="utf-8").read()
    if START not in readme or END not in readme:
        print("error: README.md lacks the table markers")
        return 1
    head, rest = readme.split(START, 1)
    tail = rest.split(END, 1)[1]
    new = head + START + "\n\n" + tables(reg) + "\n\n" + END + tail
    if new != readme:
        if "--write" in sys.argv:
            open(path, "w", encoding="utf-8", newline="\n").write(new)
            print("README.md: tables rewritten")
        else:
            errors.append("README.md's tables are out of date: run python tools/check.py --write")
            print("error:", errors[-1])
    print("ok" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
