# Equifax breach (2017)

**Topic:** patching, web  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In 2017 attackers broke into Equifax, one of the big credit bureaus, through an online dispute portal and accessed personal information of at least 145.5 million people. [KNOWN: GAO-18-559 summary]

## How they got in and what went wrong

- Equifax's own investigation named four big factors: identification, detection, segmenting of access to databases, and data governance. [KNOWN: GAO-18-559 summary]
- The way in was a known, already-patched bug in Apache Struts, a web framework, that Equifax hadn't patched on the portal. [INFERRED: widely reported and covered in GAO's full report, which our checker couldn't open; re-check]
- An expired certificate on a network monitoring device meant encrypted traffic wasn't being inspected, which helped the theft go unnoticed. [INFERRED: same as above; re-check in the full report]

## ATT&CK techniques involved

- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts
- [T1048](https://attack.mitre.org/techniques/T1048/) Exfiltration Over Alternative Protocol

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Patch internet-facing systems fast, especially when a fix is public.
- Know what software you run (asset and software inventory). You can't patch what you don't know you have.
- Monitoring tools need maintenance too. A blind sensor is no sensor.

## Practice it

[Lab 10](../labs/10-kev-patch-priorities.md) (patch priorities) and [Lab 5](../labs/05-network-sensor-zeek-suricata.md) (keep your sensor healthy).

## Sources

- https://www.gao.gov/products/gao-18-559

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
