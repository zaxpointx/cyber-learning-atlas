# Snowflake customer data theft (UNC5537) (2024)

**Topic:** cloud, identity  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In 2024 a criminal group tracked as UNC5537 stole data from many companies' Snowflake cloud database accounts and tried to extort them. Snowflake's own platform was not shown to be breached. [KNOWN: Mandiant report]

## How they got in and what went wrong

- The group used usernames and passwords stolen earlier by infostealer malware on people's computers. [KNOWN: Mandiant]
- The affected accounts did not have MFA turned on, and some credentials were years old and never rotated. [KNOWN: Mandiant]

## ATT&CK techniques involved

- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1567](https://attack.mitre.org/techniques/T1567/) Exfiltration Over Web Service

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Cloud accounts need MFA just like VPNs.
- Infostealer malware on one contractor's home PC can expose a company's cloud.
- Rotate old credentials.

## Practice it

Audit your own accounts: which have MFA, which have old passwords? Write it up as a mini risk report.

## Sources

- https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
