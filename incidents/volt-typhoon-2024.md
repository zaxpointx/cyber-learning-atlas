# Volt Typhoon pre-positioning in U.S. critical infrastructure (2024)

**Topic:** apt, ics, living-off-the-land  
**Level:** intermediate  
**Last checked:** 2026-11-22

## What happened

In February 2024, CISA, NSA, FBI and partners warned that a Chinese state-sponsored group called Volt Typhoon was hiding inside U.S. critical infrastructure networks (communications, energy, water, transportation), apparently to be ready for disruption in a future crisis. [KNOWN: CISA AA24-038A]

## How they got in and what went wrong

- They often got in through internet-facing network devices and VPN appliances. [KNOWN: AA24-038A]
- They used "living off the land": built-in tools and valid accounts instead of malware, so they blended in. [KNOWN: AA24-038A]
- They stole credentials, including the Active Directory database, to move around. [KNOWN: AA24-038A]

## ATT&CK techniques involved

- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1003](https://attack.mitre.org/techniques/T1003/) OS Credential Dumping
- [T1021](https://attack.mitre.org/techniques/T1021/) Remote Services
- [T1059](https://attack.mitre.org/techniques/T1059/) Command and Scripting Interpreter

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Normal admin tools used at strange times or from strange places are the signal. You need a baseline of normal.
- Old, unpatched edge devices are open doors.
- Defenders have to think about disruption, not just data theft.

## Practice it

[Lab 7](../labs/07-endpoint-visibility-wazuh-osquery.md): build a baseline of normal process activity on a lab VM, then spot changes.

## Sources

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
