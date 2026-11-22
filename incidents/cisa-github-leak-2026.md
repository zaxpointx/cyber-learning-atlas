# CISA credentials leaked in a contractor's public GitHub repo (2026)

**Topic:** secrets, devsecops, cloud  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In May 2026, a contractor uploaded copies of a CISA build and deployment repository, including admin and build credentials and cloud keys, to a personal public GitHub repository. A security researcher found it and it was reported through a journalist. CISA published its own lessons learned in July 2026. [KNOWN: CISA blog post, July 9, 2026]

## How they got in and what went wrong

- The person was trying to automate building cloud infrastructure and copied the repo, secrets included, to a personal account. [KNOWN: CISA]
- CISA took the repo down, reset and rotated credentials across every environment the person administered, and limited uploads to public code sites. [KNOWN: CISA]
- CISA says logs showed the leaked credentials weren't used outside its environments and no customer or mission data was exposed. [KNOWN: CISA]

## ATT&CK techniques involved

- [T1552](https://attack.mitre.org/techniques/T1552/) Unsecured Credentials
- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Never put secrets (keys, passwords, tokens) in a repo, even a "temporary" one.
- Turn on secret scanning. Companies scan public GitHub constantly, and so do attackers.
- This is very relevant if you build with AI agents: agents can copy `.env` files and keys into commits if you don't stop them. [INFERRED]

## Practice it

[Lab 12](../labs/12-secrets-and-supply-chain.md): run a secret scanner on your own repos and add a pre-commit check.

## Sources

- https://www.cisa.gov/news-events/news/lessons-cisas-cyber-incident

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
