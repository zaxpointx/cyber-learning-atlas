# Change Healthcare ransomware (2024)

**Topic:** ransomware, identity, healthcare  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In February 2024, ransomware hit Change Healthcare, which processes a huge share of U.S. medical claims. Pharmacies and providers across the country were disrupted. [KNOWN: UnitedHealth Group CEO's Senate testimony]

## How they got in and what went wrong

- On February 12, attackers used stolen credentials to log into a Citrix remote-access portal that did not have multi-factor authentication. [KNOWN: CEO's written testimony, May 1, 2024]
- They moved around and stole data, then deployed ransomware nine days later, on February 21. [KNOWN: testimony]
- The company paid a ransom. [KNOWN: testimony]

## ATT&CK techniques involved

- [T1133](https://attack.mitre.org/techniques/T1133/) External Remote Services
- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1486](https://attack.mitre.org/techniques/T1486/) Data Encrypted for Impact
- [T1567](https://attack.mitre.org/techniques/T1567/) Exfiltration Over Web Service

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Same lesson as Colonial Pipeline, three years later: one internet-facing login without MFA.
- Companies you buy (acquisitions) bring their old systems and old gaps with them. [INFERRED from the testimony's mention of a legacy server]
- Nine days between entry and ransomware is a window where good detection could have caught it.

## Practice it

[Lab 4](../labs/04-logs-and-brute-force.md), then write a detection idea for "successful remote login without MFA from a new place".

## Sources

- https://www.finance.senate.gov/imo/media/doc/0501_witty_testimony.pdf

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
