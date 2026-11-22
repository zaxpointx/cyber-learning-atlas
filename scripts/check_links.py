#!/usr/bin/env python3
"""Check external https links in Markdown and the index.

Fails only on links that are clearly dead (404, 410, or DNS failure).
Sites that block bots (403, 429, 5xx, timeouts) are reported as warnings,
because many government and vendor sites refuse automated checkers.
"""
import concurrent.futures as cf
import csv
import re
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"https://[^\s)\]>\"'`|]+")
UA = "Mozilla/5.0 (compatible; cyber-learning-atlas-linkcheck/1.0; +https://github.com/zaxpointx/cyber-learning-atlas)"
SKIP_PREFIXES = ("https://github.com/zaxpointx/cyber-learning-atlas",)


def collect():
    urls = set()
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        for u in URL.findall(p.read_text(encoding="utf-8")):
            urls.add(u.rstrip(".,;:"))
    with (ROOT / "index" / "entries.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            urls.add(r["url"])
    return sorted(u for u in urls if not u.startswith(SKIP_PREFIXES))


def check(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return url, r.status, ""
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 404, 405, 429, 500, 501, 503):
                continue
            return url, e.code, ""
        except urllib.error.URLError as e:
            if isinstance(e.reason, socket.gaierror):
                return url, "dns", str(e.reason)
            if method == "HEAD":
                continue
            return url, "error", str(e.reason)
        except Exception as e:  # timeouts and other network trouble
            if method == "HEAD":
                continue
            return url, "error", str(e)
    return url, "error", "unreachable"


def main():
    urls = collect()
    dead, warn = [], []
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for url, status, note in ex.map(check, urls):
            if status in (404, 410, "dns"):
                dead.append((url, status, note))
            elif not (isinstance(status, int) and 200 <= status < 400):
                warn.append((url, status, note))
    print(f"checked {len(urls)} links: {len(dead)} dead, {len(warn)} warnings")
    for u, s, n in warn:
        print(f"  warn {s} {u} {n}")
    for u, s, n in dead:
        print(f"  DEAD {s} {u} {n}")
    sys.exit(1 if dead else 0)


if __name__ == "__main__":
    main()
