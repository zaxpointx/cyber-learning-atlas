# Colonial Pipeline ransomware (2021)

**Topic:** ransomware, ics  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In May 2021 a ransomware attack hit Colonial Pipeline, which carries fuel across the eastern U.S. The company shut the pipeline down as a precaution, which led to fuel shortages and panic buying. [KNOWN: Senate hearing record]

## How they got in and what went wrong

- The CEO told the Senate the attackers got in through a legacy VPN account that used only a password, no multi-factor authentication. [KNOWN: Senate HSGAC hearing, June 8, 2021]
- The ransomware hit the business IT side. The pipeline itself was shut down to be safe. [KNOWN: hearing record]
- The company paid a ransom, and the Justice Department later seized back about $2.3 million of it. [KNOWN: DOJ press release]

## ATT&CK techniques involved

- [T1133](https://attack.mitre.org/techniques/T1133/) External Remote Services
- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1486](https://attack.mitre.org/techniques/T1486/) Data Encrypted for Impact

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- One old account without MFA can take down critical infrastructure.
- Clean up accounts nobody uses anymore.
- Even if the industrial side is never touched, an IT hack can still stop operations.

## Practice it

[Lab 4](../labs/04-logs-and-brute-force.md) (watch your own login logs) and [Lab 11](../labs/11-tabletop-from-a-real-incident.md) (run this as a tabletop).

## Sources

- https://www.govinfo.gov/content/pkg/CHRG-117shrg46569/html/CHRG-117shrg46569.htm
- https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
