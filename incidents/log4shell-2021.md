# Log4Shell (Log4j) (2021)

**Topic:** vulnerability, open-source  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In December 2021 a bug in Log4j, a very common Java logging library, let attackers run code on servers just by getting the server to log a special text string. It was tracked as CVE-2021-44228. [KNOWN: CISA Log4j guidance]

## How they got in and what went wrong

- A feature that looked up data while logging could be tricked into loading attacker code from the internet. [KNOWN: CISA guidance]
- Because Log4j was buried inside thousands of products, many organizations didn't know where they used it. [KNOWN: CSRB Log4j review]
- The Cyber Safety Review Board concluded Log4j would remain a problem for years, because vulnerable copies would linger. [KNOWN: CSRB Log4j review, paraphrased]

## ATT&CK techniques involved

- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1105](https://attack.mitre.org/techniques/T1105/) Ingress Tool Transfer

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Keep a software bill of materials (SBOM): a list of what's inside your software.
- Volunteer-run open source holds up a lot of the internet and needs support.
- Logging can be an attack surface, not just a defense.

## Practice it

[Lab 10](../labs/10-kev-patch-priorities.md): check KEV for CVE-2021-44228 and see how it is described.

## Sources

- https://www.cisa.gov/news-events/news/apache-log4j-vulnerability-guidance
- https://www.cisa.gov/resources-tools/resources/csrb-review-december-2021-log4j-event

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
