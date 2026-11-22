# Using the KEV list to decide what to patch first

**Short answer:** there are hundreds of thousands of CVEs, but only a small slice are actually being used by attackers. CISA keeps that slice in the **Known Exploited Vulnerabilities (KEV) catalog**. If you only have time to patch a few things, patch what is on KEV first.

## What KEV is

- A public list from CISA of vulnerabilities with reliable evidence of real-world exploitation. [KNOWN: https://www.cisa.gov/known-exploited-vulnerabilities-catalog]
- U.S. federal agencies are required to fix KEV entries by a due date. Everyone else uses it as a free priority list. [KNOWN: https://www.cisa.gov/known-exploited-vulnerabilities]
- Free to download as JSON or CSV, and mirrored on GitHub under CC0. [KNOWN: https://github.com/cisagov/kev-data]

## What the numbers looked like when we checked (2026-11-22)

We downloaded the KEV JSON feed (catalog version 2026.11.20) and counted. [KNOWN: our own count from the CISA feed]

- **1,790** vulnerabilities on the list.
- **361** are marked as known to be used in ransomware campaigns.
- Most-listed vendors: Microsoft (391), Cisco (104), Apple (96), Adobe (83), Google (77).
- **37** entries are for Cisco IOS or IOS XE software (not counting IOS XR), and **9** of those are SNMP bugs (remote code execution or denial of service).

**Key takeaway:** network gear is a big target. That is why [Lab 2](../labs/02-harden-your-cisco-router.md) starts by turning off old SNMP versions and the web management server on your router.

## Why it matters right now

The 2026 Verizon DBIR found that exploiting vulnerabilities became the top way into breaches (31%), passing stolen credentials for the first time in the report's 19 years. It also found only 26% of KEV vulnerabilities were fully fixed by organizations in its data, with a median of 43 days to fix. [KNOWN: https://www.verizon.com/about/news/breach-industry-wide-dbir-finds]

## Three free signals to combine

| Signal | What it tells you | Where |
|---|---|---|
| **KEV** | Attackers are using it right now | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| **EPSS** | A probability score for how likely a CVE is to be exploited soon | https://www.first.org/epss/ |
| **CVSS (in NVD)** | How bad it would be if exploited | https://nvd.nist.gov/ |

A simple rule of thumb: **KEV first, then high EPSS, then high CVSS.** [INFERRED: common practice, not an official rule]

## Try it

```bash
# list KEV entries for Cisco IOS (downloads the public CISA feed)
python3 scripts/kev_lookup.py --vendor cisco --product ios

# only the ones tied to ransomware
python3 scripts/kev_lookup.py --ransomware
```

Then do [Lab 10](../labs/10-kev-patch-priorities.md), which turns this into a patch plan for your own lab machines.
