# MOVEit Transfer mass data theft (Cl0p) (2023)

**Topic:** ransomware, web, vulnerability  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

Starting in late May 2023, the Cl0p ransomware gang exploited an unknown bug (a zero-day) in MOVEit Transfer, a file transfer product, and stole data from a huge number of organizations. [KNOWN: CISA AA23-158A]

## How they got in and what went wrong

- The bug was a SQL injection flaw, CVE-2023-34362, in the internet-facing web app. [KNOWN: AA23-158A]
- They installed a web shell called LEMURLOOT to steal data. [KNOWN: AA23-158A]
- They focused on stealing and threatening to leak data, not just encrypting it. [KNOWN: AA23-158A]

## ATT&CK techniques involved

- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1505](https://attack.mitre.org/techniques/T1505/) Server Software Component
- [T1567](https://attack.mitre.org/techniques/T1567/) Exfiltration Over Web Service

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- File transfer servers hold sensitive data and face the internet: prime targets.
- SQL injection is an old bug class that still causes massive breaches.
- Extortion without encryption is still ransomware in practice.

## Practice it

[Lab 9](../labs/09-web-app-testing-juice-shop.md): see SQL injection safely in OWASP Juice Shop on your own machine.

## Sources

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
