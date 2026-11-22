#!/usr/bin/env python3
"""Structure checks for the cyber-learning-atlas. No network access.

Checks:
  1. Required files exist.
  2. index/entries.csv has the right columns, valid values, unique ids, real paths, https URLs.
  3. index/entries.json matches the CSV (run scripts/build_index.py if not).
  4. Every relative Markdown link points to a file that exists.
  5. No em dashes or en dashes in Markdown, CSV or JSON (house style).
  6. Every lab has Goal, Steps (or Part), and Write-up sections.
  7. Every incident page has the required sections and at least one source.
Exit code 1 on any error.
"""
import csv
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md", "AGENTS.md", "GLOSSARY.md", "LICENSE", "NOTICE.md",
    "techniques/README.md", "techniques/kev.md", "incidents/README.md", "incidents/yearly-reports.md",
    "tools/README.md", "practice/README.md", "research/README.md", "labs/README.md",
    "labs/SAFETY.md", "labs/WRITEUP-TEMPLATE.md", "real-world/README.md",
    "index/entries.csv", "index/entries.json",
]
COLUMNS = ["id", "type", "title", "topic", "level", "cost", "license", "platform_fit",
           "url", "path", "tag", "date_checked", "summary"]
TYPES = {"technique", "defense", "incident", "report", "tool", "platform", "research", "lab", "real-world", "guide"}
LEVELS = {"beginner", "intermediate", "advanced"}
FITS = {"arm-ok", "arm-partial", "x86-only", "web", "n/a", "unknown"}
TAGS = {"KNOWN", "INFERRED", "UNKNOWN"}
COSTS = {"free", "freemium", "paid"}
DASHES = re.compile("[\u2014\u2013]")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

errors = []


def err(msg):
    errors.append(msg)


def check_required():
    for p in REQUIRED:
        if not (ROOT / p).exists():
            err(f"missing required file: {p}")


def check_csv():
    path = ROOT / "index" / "entries.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            err(f"entries.csv columns are {reader.fieldnames}, expected {COLUMNS}")
            return
        seen = set()
        for n, r in enumerate(reader, start=2):
            where = f"entries.csv line {n} ({r.get('id')})"
            for c in COLUMNS:
                if not (r.get(c) or "").strip():
                    err(f"{where}: empty column '{c}'")
            if r["id"] in seen:
                err(f"{where}: duplicate id")
            seen.add(r["id"])
            if r["type"] not in TYPES:
                err(f"{where}: bad type '{r['type']}'")
            if r["level"] not in LEVELS:
                err(f"{where}: bad level '{r['level']}'")
            if r["platform_fit"] not in FITS:
                err(f"{where}: bad platform_fit '{r['platform_fit']}'")
            if r["tag"] not in TAGS:
                err(f"{where}: bad tag '{r['tag']}'")
            if r["cost"] not in COSTS:
                err(f"{where}: bad cost '{r['cost']}'")
            if not r["url"].startswith("https://"):
                err(f"{where}: url must start with https://")
            if not (ROOT / r["path"]).exists():
                err(f"{where}: path does not exist: {r['path']}")
            try:
                d = date.fromisoformat(r["date_checked"])
                if d > date.today():
                    err(f"{where}: date_checked is in the future")
            except ValueError:
                err(f"{where}: date_checked not YYYY-MM-DD")


def check_json_in_sync():
    current = (ROOT / "index" / "entries.json").read_text(encoding="utf-8")
    if current != build_index.build():
        err("index/entries.json is out of date: run python3 scripts/build_index.py")


def text_files():
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        if p.suffix in {".md", ".csv", ".json"}:
            yield p


def check_links_and_dashes():
    for p in text_files():
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT)
        for i, line in enumerate(text.splitlines(), start=1):
            if DASHES.search(line):
                err(f"{rel}:{i}: em or en dash found (house style: use commas or periods)")
        if p.suffix != ".md":
            continue
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            if not (p.parent / file_part).resolve().exists():
                err(f"{rel}: broken relative link -> {target}")


def check_sections():
    for p in sorted((ROOT / "labs").glob("[0-9][0-9]-*.md")):
        t = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT)
        if "**Goal:**" not in t:
            err(f"{rel}: missing **Goal:**")
        if "## Steps" not in t and "## Part" not in t:
            err(f"{rel}: missing ## Steps")
        if "## Write-up" not in t:
            err(f"{rel}: missing ## Write-up")
    for p in sorted((ROOT / "incidents").glob("*.md")):
        if p.name in {"README.md", "yearly-reports.md"}:
            continue
        t = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT)
        for s in ["## What happened", "## Lessons", "## Sources"]:
            if s not in t:
                err(f"{rel}: missing {s}")
        if not re.search(r"## Sources\s+- https://", t):
            err(f"{rel}: needs at least one https source under ## Sources")


def main():
    check_required()
    if not errors:
        check_csv()
        check_json_in_sync()
    check_links_and_dashes()
    check_sections()
    if errors:
        print(f"{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("repo structure OK")


if __name__ == "__main__":
    main()
