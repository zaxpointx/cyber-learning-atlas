#!/usr/bin/env python3
"""Look up entries in CISA's Known Exploited Vulnerabilities (KEV) catalog.

Downloads the public KEV JSON feed (CC0) and filters it. Read-only, no keys,
no scanning. Example:
    python3 scripts/kev_lookup.py --vendor cisco --product ios
    python3 scripts/kev_lookup.py --ransomware --since 2026-01-01
"""
import argparse
import json
import sys
import urllib.request

FEED = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def load(path=None):
    if path:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    req = urllib.request.Request(FEED, headers={"User-Agent": "cyber-learning-atlas-kev-lookup"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--vendor", help="text to match in vendorProject (case-insensitive)")
    p.add_argument("--product", help="text to match in product (case-insensitive)")
    p.add_argument("--ransomware", action="store_true", help="only entries marked Known ransomware use")
    p.add_argument("--since", help="only entries added on or after YYYY-MM-DD")
    p.add_argument("--file", help="use a local copy of the KEV JSON instead of downloading")
    p.add_argument("--csv", action="store_true", help="print CSV instead of a table")
    a = p.parse_args()

    data = load(a.file)
    rows = []
    for v in data["vulnerabilities"]:
        if a.vendor and a.vendor.lower() not in v["vendorProject"].lower():
            continue
        if a.product and a.product.lower() not in v["product"].lower():
            continue
        if a.ransomware and v.get("knownRansomwareCampaignUse") != "Known":
            continue
        if a.since and v["dateAdded"] < a.since:
            continue
        rows.append(v)

    rows.sort(key=lambda v: v["dateAdded"], reverse=True)
    if a.csv:
        print("cveID,vendorProject,product,dateAdded,ransomware,vulnerabilityName")
        for v in rows:
            name = v["vulnerabilityName"].replace('"', "'")
            print(f'{v["cveID"]},"{v["vendorProject"]}","{v["product"]}",{v["dateAdded"]},{v.get("knownRansomwareCampaignUse","")},"{name}"')
    else:
        for v in rows:
            flag = "R" if v.get("knownRansomwareCampaignUse") == "Known" else " "
            print(f'{v["dateAdded"]}  {flag}  {v["cveID"]:<16} {v["vendorProject"]} {v["product"]}: {v["vulnerabilityName"]}')
    print(f"\n{len(rows)} of {data['count']} KEV entries matched (catalog {data['catalogVersion']}). R = known ransomware use.", file=sys.stderr)


if __name__ == "__main__":
    main()
