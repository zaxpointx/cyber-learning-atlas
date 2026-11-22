#!/usr/bin/env python3
"""Regenerate index/entries.json from index/entries.csv (the CSV is the source of truth)."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "index" / "entries.csv"
JSON = ROOT / "index" / "entries.json"


def build():
    with CSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["topic"] = [t for t in r["topic"].split(";") if t]
    out = {
        "name": "cyber-learning-atlas index",
        "description": "Every entry in the repo with type, topic, level, source URL and date checked. Generated from entries.csv.",
        "count": len(rows),
        "entries": rows,
    }
    return json.dumps(out, indent=2, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    JSON.write_text(build(), encoding="utf-8")
    print(f"wrote {JSON.relative_to(ROOT)}")
