# XZ Utils backdoor (2024)

**Topic:** supply-chain, open-source, linux  
**Level:** intermediate  
**Last checked:** 2026-11-22

## What happened

In March 2024 a backdoor was found in versions 5.6.0 and 5.6.1 of XZ Utils, a compression library included in many Linux systems. It was caught before it reached most stable Linux releases. [KNOWN: CISA alert, March 29, 2024]

## How they got in and what went wrong

- The upstream xz repository and release tarballs were backdoored, and one part of the backdoor existed only in the distributed tarballs, not in the git source most people read. [KNOWN: oss-security disclosure] Later public analyses describe the person behind it spending years earning maintainer trust. [INFERRED: from later reporting, not the original disclosure]
- The backdoor targeted SSH logins on some Linux systems. [KNOWN: oss-security disclosure]
- A software engineer noticed SSH logins on a test system were using a lot of CPU and getting slower, dug in, and found it. [KNOWN: oss-security disclosure]

## ATT&CK techniques involved

- [T1195](https://attack.mitre.org/techniques/T1195/) Supply Chain Compromise

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Curiosity about small weird things saves the day. Investigate the odd slowdown.
- Release tarballs can differ from the source code you can read in the repo.
- Open-source maintainers are often overworked volunteers, which attackers can exploit socially.

## Practice it

[Lab 12](../labs/12-secrets-and-supply-chain.md): check package versions on your Parrot VM and learn how to verify signatures.

## Sources

- https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094
- https://www.openwall.com/lists/oss-security/2024/03/29/4

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
