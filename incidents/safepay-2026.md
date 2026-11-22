# SafePay ransomware (2026)

**Topic:** ransomware  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In October 2026, FBI, CISA, the Secret Service and partners warned about SafePay, one of the most active ransomware groups of 2026, with at least 600 victims across many sectors. [KNOWN: CISA AA26-293A]

## How they got in and what went wrong

- They get in by stealing or guessing passwords, exploiting edge devices like firewalls and VPNs, and phishing. Named bugs include Cisco ASA/FTD (CVE-2020-3259, CVE-2023-20269), Veeam (CVE-2023-27532, CVE-2024-40711) and SonicWall (CVE-2024-40766). [KNOWN: AA26-293A]
- They use normal tools (RClone, WinSCP, AnyDesk, TeamViewer) to move data and stay in. [KNOWN: AA26-293A]
- They stop shadow copies and even factory-reset network storage holding backups before encrypting. [KNOWN: AA26-293A]

## ATT&CK techniques involved

- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1110](https://attack.mitre.org/techniques/T1110/) Brute Force
- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1219](https://attack.mitre.org/techniques/T1219/) Remote Access Tools
- [T1048](https://attack.mitre.org/techniques/T1048/) Exfiltration Over Alternative Protocol
- [T1567](https://attack.mitre.org/techniques/T1567/) Exfiltration Over Web Service
- [T1490](https://attack.mitre.org/techniques/T1490/) Inhibit System Recovery
- [T1486](https://attack.mitre.org/techniques/T1486/) Data Encrypted for Impact

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Edge devices and backup servers are top targets. Patch the KEV entries for them first.
- Offline, immutable backups that you actually test are what save you.
- Legit remote-access tools showing up where they shouldn't is a big red flag.

## Practice it

[Lab 10](../labs/10-kev-patch-priorities.md) (look up the five CVEs in KEV) and [Lab 11](../labs/11-tabletop-from-a-real-incident.md) (tabletop this one).

## Sources

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a
- https://www.cisa.gov/news-events/news/cisa-fbi-and-partners-warn-organizations-safepay-ransomware-actors-targeting-multiple-critical

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
