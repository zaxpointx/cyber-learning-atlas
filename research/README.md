# Research and talks worth your time

Grouped from "read this first" to "deep end". Everything here is free to read without signing up unless marked.

**Key takeaway:** read one NIST or CISA guide a month, watch one conference talk a week, and skim CISA advisories as they come out. That habit alone puts you ahead of most entry-level applicants. [INFERRED]

## 1. Frameworks and guides (the rulebooks)

| Resource | What it is | Why read it | Level |
|---|---|---|---|
| [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/cyberframework) | The six big functions of security: Govern, Identify, Protect, Detect, Respond, Recover | The shared language every security team uses. Shows up on Security+. | Beginner |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Incident response recommendations, built around CSF 2.0 | How real teams handle incidents. Use it for Lab 11. | Beginner |
| [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) | Technical guide to security testing | How professional testing is planned and scoped (it's old, from 2008, but the ideas hold). | Intermediate |
| [NIST SP 800-63-4](https://csrc.nist.gov/pubs/sp/800/63/4/final) | Digital identity guidelines: passwords, MFA, identity proofing | Why phishing-resistant MFA matters. | Intermediate |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | The huge catalog of security controls used by the federal government and labs | Skim it. Federal sites like ORNL and Y-12 live by controls like these. [INFERRED] | Advanced |
| [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | Operational technology (industrial control) security | The ICS and grid side, close to ORNL's grid work. | Advanced |
| [CIS Critical Security Controls](https://www.cisecurity.org/controls) | A prioritized list of what to do first | Practical, ordered checklist. | Beginner |
| [OWASP Top 10:2025](https://owasp.org/Top10/2025/) | The ten biggest web app risk categories | Pairs with Lab 9 and PortSwigger. | Beginner |
| [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) | How to test web apps step by step | Deeper web testing method. | Intermediate |
| [CISA Cyber Essentials](https://www.cisa.gov/cyber-essentials) | Plain guide for small organizations | Great for explaining security to non-tech people. | Beginner |
| [CISA #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) | Ransomware prevention and response checklist | Turns the incidents folder into actions. | Beginner |
| [CISA Secure by Design](https://www.cisa.gov/securebydesign) | Pushes vendors to ship safer defaults | How security is shifting onto software makers. | Intermediate |
| [CISA communications infrastructure hardening guidance](https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure) | Router and switch hardening and visibility for network gear | Read before Lab 2. | Intermediate |
| [Cisco IOS hardening guide](https://sec.cloudapps.cisco.com/security/center/resources/IOS_hardening) | Cisco's own guide to hardening IOS devices | Directly applies to your 1941. | Intermediate |

## 2. Threat knowledge bases

| Resource | What it is |
|---|---|
| [MITRE ATT&CK](https://attack.mitre.org/) | How attackers operate. This repo uses v20.1. |
| [MITRE D3FEND](https://d3fend.mitre.org/) | How defenders respond, mapped to ATT&CK. |
| [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) | Industrial and grid attack techniques. |
| [CISA Cybersecurity Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) | Joint government advisories with TTPs and fixes. |
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | What's being exploited now. |
| [CVE](https://www.cve.org/) and [NVD](https://nvd.nist.gov/) | The official vulnerability ID list and NIST's scoring database. |
| [FIRST EPSS](https://www.first.org/epss/) | Exploit prediction scores. |

## 3. Yearly reports

See [incidents/yearly-reports.md](../incidents/yearly-reports.md): Verizon DBIR 2026, Mandiant M-Trends 2026, ENISA.

## 4. Conference talks (free recordings)

| Source | What you'll find | Start with |
|---|---|---|
| [DEF CON media server](https://media.defcon.org/) | Slides, videos and materials from every DEF CON, the biggest hacker conference. | The "villages" talks (ICS Village, Car Hacking Village, Blue Team Village) are often beginner friendly. [INFERRED] |
| [Black Hat on YouTube](https://www.youtube.com/@BlackHatOfficialYT) | Research talks from Black Hat USA, Europe and Asia. | Search for "keynote" and for topics you're labbing. |
| [USENIX Security papers](https://www.usenix.org/conferences/byname/108) | Top academic security research, open access. | Read the abstract and conclusion first. |
| [SANS posters](https://www.sans.org/posters/) | Cheat-sheet posters on forensics, Linux, Windows logging. | Some need a free SANS account. Skip those under this repo's rules. |

## 5. Research feeds

| Feed | What it is |
|---|---|
| [arXiv cs.CR (recent)](https://arxiv.org/list/cs.CR/recent) | New cryptography and security preprints every day. Not peer reviewed yet. |
| [Google Project Zero blog](https://googleprojectzero.blogspot.com/) | Deep vulnerability research from Google's bug hunting team. Advanced, but amazing to read. |
| [Cisco Talos blog](https://blog.talosintelligence.com/) | Threat research, including attacks on network devices. |
| [Detection Engineering Weekly](https://www.detectionengineering.net/) | A weekly newsletter on writing detections. The web archive is public. |

## 6. Supply chain and DevSecOps (for someone who builds with AI agents)

| Resource | What |
|---|---|
| [SLSA](https://slsa.dev/) | A framework for making software builds tamper resistant. |
| [OpenSSF](https://openssf.org/) and [Scorecard](https://scorecard.dev/) | Open source security foundation and its project grader. |
| [GitHub secret scanning docs](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) | How GitHub catches leaked keys. See the [CISA GitHub leak incident](../incidents/cisa-github-leak-2026.md). |
