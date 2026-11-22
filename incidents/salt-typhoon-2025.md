# Salt Typhoon and telecom router compromises (2025)

**Topic:** apt, network-devices  
**Level:** intermediate  
**Last checked:** 2026-11-22

## What happened

In August 2025, NSA, CISA, FBI and many international partners warned that Chinese state-sponsored actors were compromising large telecom backbone routers and edge routers worldwide to feed an espionage system. Industry tracks overlapping activity as Salt Typhoon, among other names. [KNOWN: CISA AA25-239A]

## How they got in and what went wrong

- They exploited known bugs in edge devices, including Cisco IOS XE (CVE-2023-20198 and CVE-2023-20273), Ivanti and Palo Alto products. [KNOWN: AA25-239A]
- They changed router configs to keep access: editing ACLs to allow their IPs, opening SSH on odd high ports, adding tunnels like GRE. [KNOWN: AA25-239A]
- They abused SNMP, and many hacked devices still used default community strings like "public" and "private". [KNOWN: AA25-239A]

## ATT&CK techniques involved

- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1098](https://attack.mitre.org/techniques/T1098/) Account Manipulation
- [T1572](https://attack.mitre.org/techniques/T1572/) Protocol Tunneling
- [T1021](https://attack.mitre.org/techniques/T1021/) Remote Services

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Routers are computers, and attackers live on them for years.
- Keep a known-good copy of your router config and compare it regularly.
- The advisory's D3FEND table is basically a router hardening checklist: SNMPv3, no default passwords, disable unused services, isolate management. [KNOWN: AA25-239A]

## Practice it

[Lab 2](../labs/02-harden-your-cisco-router.md). This advisory is the best real-world reason to do it.

## Sources

- https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
