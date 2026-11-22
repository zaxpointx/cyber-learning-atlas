# Ukraine power grid attack (2015)

**Topic:** ics, grid  
**Level:** intermediate  
**Last checked:** 2026-11-22

## What happened

On December 23, 2015, attackers broke into three regional power distribution companies in Ukraine and switched off power to about 225,000 customers for hours. [KNOWN: CISA ICS alert IR-ALERT-H-16-056-01]

## How they got in and what went wrong

- Attackers got into the business networks first, and public reports say spear phishing with BlackEnergy malware was involved. CISA was careful to say it could not confirm BlackEnergy's exact role in the outage. [KNOWN: CISA alert]
- They used remote access to operate the grid control software and open breakers. [KNOWN: CISA alert]
- Then they wiped systems with KillDisk and broke serial-to-Ethernet devices at substations so operators couldn't easily recover. [KNOWN: CISA alert]

## ATT&CK techniques involved

- [T1566](https://attack.mitre.org/techniques/T1566/) Phishing
- [T1133](https://attack.mitre.org/techniques/T1133/) External Remote Services
- [T1485](https://attack.mitre.org/techniques/T1485/) Data Destruction
- [T1490](https://attack.mitre.org/techniques/T1490/) Inhibit System Recovery

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Business IT and grid control networks need hard separation.
- Attackers plan for recovery too. Breaking the tools you use to recover is part of the attack.
- Grid attacks are real, not movie plots. This is the kind of risk ORNL's grid security groups study.

## Practice it

Read ATT&CK for ICS (https://attack.mitre.org/matrices/ics/) and map this attack onto it. Then compare with the ORNL grid deep dive in the [real world layer](../real-world/README.md).

## Sources

- https://www.cisa.gov/news-events/ics-alerts/ir-alert-h-16-056-01
- https://attack.mitre.org/matrices/ics/

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
