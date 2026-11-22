# CrowdStrike faulty update outage (not an attack) (2024)

**Topic:** resilience, change-management  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

On July 19, 2024, a bad content update to CrowdStrike's Falcon security sensor crashed Windows computers worldwide. Microsoft estimated about 8.5 million Windows devices were affected. This was a mistake, not a cyberattack. [KNOWN: CISA alert; Microsoft blog]

## How they got in and what went wrong

- A new template expected 21 input fields, but the sensor code only provided 20, causing an out-of-bounds memory read that crashed Windows. [KNOWN: CrowdStrike root cause analysis]
- The validation step didn't catch the mismatch. [KNOWN: CrowdStrike RCA]
- Because the sensor runs deep in the system, the crash happened at boot, and many machines needed hands-on fixes. [INFERRED]

## ATT&CK techniques involved

None. This was not an attack.

## Lessons

- Availability is part of security (the A in the CIA triad).
- Roll updates out in stages, even security updates.
- Have a plan to recover machines that won't boot.

## Practice it

Use VM snapshots in every lab ([Lab 0](../labs/00-safe-lab-setup.md)). That is your own staged rollout and rollback.

## Sources

- https://www.cisa.gov/news-events/alerts/2024/07/19/widespread-it-outage-due-crowdstrike-update
- https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf
- https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
