# Lapsus$ extortion attacks (2022)

**Topic:** identity, social-engineering  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

From late 2021 into 2022, a loose group called Lapsus$ broke into dozens of big companies and agencies, stole data and source code, and demanded payment. The Cyber Safety Review Board noted the group included several juveniles. [KNOWN: CSRB Lapsus$ review]

## How they got in and what went wrong

- They used SIM swapping (getting a phone carrier to move a victim's number) to grab text-message and voice MFA codes. [KNOWN: CSRB]
- They bought access and stolen credentials from criminal markets, and tricked employees and help desks. [KNOWN: CSRB]
- The Board found that organizations using app-based or token-based MFA and strong detection held up much better. [KNOWN: CSRB]

## ATT&CK techniques involved

- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1566](https://attack.mitre.org/techniques/T1566/) Phishing
- [T1111](https://attack.mitre.org/techniques/T1111/) Multi-Factor Authentication Interception

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Text-message MFA is better than nothing but is weak. Use an authenticator app or a security key.
- Help desks are a target. Identity checks for password resets matter.
- You don't need fancy tools to do huge damage. Basic social engineering works.

## Practice it

Set up app-based or key-based MFA on your own accounts, then read the CSRB report's recommendations and pick three you could apply to your home lab.

## Sources

- https://www.cisa.gov/resources-tools/resources/review-attacks-associated-lapsus-and-related-threat-groups-report

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
