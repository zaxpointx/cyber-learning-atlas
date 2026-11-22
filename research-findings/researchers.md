# Who publishes the most learnable security research?

Answers issue #6.
Checked: 2026-11-22. Every link below was opened on that date.

Tags:
[KNOWN] means it is on the linked page.
[INFERRED] means my reasoning from what I saw.
[UNKNOWN] means I looked and could not find it.

---

## The short answer

The best teams to learn from share three things.
They show their work step by step.
They give away the tools or rules they used.
And they tie it to MITRE ATT&CK, so it maps onto your labs.

My top 5 for you right now:

1. **The DFIR Report** (real intrusions, start to finish)
2. **Red Canary** (Atomic Red Team plus the yearly Threat Detection Report)
3. **Elastic Security Labs** (open detection rules you can read)
4. **Objective-See** (Mac security, free open-source tools)
5. **Cisco Talos** (weekly newsletter, and you own a Cisco router)

Save **Google Project Zero** and **watchTowr Labs** for later.
They are brilliant but advanced. [INFERRED]

---

## What is new compared to research/README.md

`research/README.md` already lists two of these:
Google Project Zero and Cisco Talos.

Everything else in this file is new.
That includes 12 more teams, one university lab,
and the individuals section at the bottom.

One fix for the README:
the Project Zero blog moved.
The old link redirects to https://projectzero.google/ [KNOWN]

---

## How to read the cards

Each team gets the same five lines.

- **What:** what they publish
- **How often:** based on recent post dates
- **Level:** beginner, intermediate or advanced
- **Lab fit:** which lab in this repo it pairs with
- **Start here:** one piece to read first

---

## Defender teams (start here)

These explain attacks so you can catch them.
They fit the home SOC labs (5 to 8) best. [INFERRED]

### The DFIR Report

- **What:** full write-ups of real intrusions. Each one has a timeline, ATT&CK technique IDs, Sigma and YARA rule names, and indicators. [KNOWN]
- **How often:** about one report every month or two in 2025 and 2026. [INFERRED from the dates on the home page]
- **Level:** beginner+ to intermediate. Plain story, real detail. [INFERRED]
- **Lab fit:** Lab 4 (brute force) and Lab 11 (tabletop).
- **Start here:** "Hide Your RDP: Password Spray Leads to RansomHub Deployment." It starts with a password spray on an exposed RDP server, which is exactly what Lab 4 teaches you to spot. [KNOWN]
  https://thedfirreport.com/2025/06/30/hide-your-rdp-password-spray-leads-to-ransomhub-deployment/
- **Open stuff:** their public Sigma rules now go straight into the main SigmaHQ repo. [KNOWN]
  https://github.com/The-DFIR-Report/Sigma-Rules
- **Note:** they also sell a private rule pack. Skip it. The free reports are enough. [KNOWN]
- Home: https://thedfirreport.com/

### Red Canary (now part of Zscaler)

- **What:** the yearly Threat Detection Report (top threats and top ATT&CK techniques, with detection advice), and the Atomic Red Team test library. [KNOWN]
- **How often:** the report is yearly. The 2026 edition is the eighth. [KNOWN] Atomic Red Team gets commits most weeks (last push 2026-11-16). [KNOWN]
- **Level:** beginner+ to intermediate. [INFERRED]
- **Lab fit:** Lab 8 (Atomic Red Team) and Lab 6 (detection rules).
- **Start here:** the 2026 Threat Detection Report summary.
  https://www.zscaler.com/blogs/cybersecurity-best-practices/2026-threat-detection-report
- **Heads up:** the redcanary.com report page I opened still showed the 2022 menus. [KNOWN] Whether the 2026 web version needs a form: [UNKNOWN]. If it asks for an email, skip it (rule 3).
- Atomic Red Team: https://github.com/redcanaryco/atomic-red-team (about 12,900 stars) [KNOWN]
- Report page: https://redcanary.com/threat-detection-report/

### Elastic Security Labs

- **What:** malware and attack write-ups, plus a public detection rules repo with more than just rules. It also has tests, hunting queries and a Python toolkit. [KNOWN]
- **How often:** several posts a week in Oct and Nov 2026. [INFERRED from listing dates]
- **Level:** intermediate. A lot of recent posts are about AI and their own product, so pick the research ones. [INFERRED]
- **Lab fit:** Lab 6 (rules) and Lab 7 (endpoint).
- **Start here:** open the `rules/` folder in the repo and read three rules for techniques you already know, like brute force (T1110).
  https://github.com/elastic/detection-rules (about 3,000 stars, pushed 2026-11-20) [KNOWN]
- Endpoint rules too: https://github.com/elastic/protections-artifacts [KNOWN]
- Blog: https://www.elastic.co/security-labs

### Cisco Talos

- **What:** threat research, vulnerability posts, Snort rules for each Patch Tuesday, and a weekly newsletter called Threat Source. [KNOWN]
- **How often:** several posts a week. Threat Source comes out every Thursday. [KNOWN]
- **Level:** beginner (newsletter) to intermediate (research). [INFERRED]
- **Lab fit:** Lab 2 (your Cisco 1941) and Lab 5 (Snort is a cousin of Suricata). [INFERRED]
- **Start here:** read one Threat Source issue a week. It mixes news, research and career talk. [KNOWN]
  https://blog.talosintelligence.com/category/threat-source-newsletter/
- Indicators on GitHub: https://github.com/Cisco-Talos/IOCs [KNOWN]
- Already in research/README.md.

### Huntress

- **What:** SOC stories from real customer incidents, plus deep threat research. [KNOWN]
- **How often:** almost daily in Nov 2026, though some posts are product news. [INFERRED from listing dates]
- **Level:** beginner (the "Cybersecurity Education" posts) to advanced (threat research). [INFERRED]
- **Lab fit:** Lab 5 (Suricata) and Lab 11 (tabletop).
- **Start here (stretch):** "Detecting Timeroasting the Hard Way" (2026-11-19). It shows how a researcher wrote Suricata rules for an Active Directory attack and tested them on captured traffic. Free to read, no login. [KNOWN] It is advanced, so read it after Lab 5. [INFERRED]
  https://www.huntress.com/blog/detecting-timeroasting
- Blog: https://www.huntress.com/blog

---

## Big threat intel teams

These track nation-state groups and big campaigns.
They are great for "what is happening right now."
Their posts assume you know the jargon. [INFERRED]

### Unit 42 (Palo Alto Networks)

- **What:** campaign research, "Threat Brief" posts on hot vulnerabilities, and trend reports. [KNOWN]
- **How often:** several posts a week. [INFERRED from listing dates]
- **Level:** intermediate. Their "top 5 initial access vectors" post uses terms like "watering hole" without explaining them. [KNOWN]
- **Lab fit:** Lab 10 (KEV) and Lab 11.
- **Start here:** "Top 5 Initial Access Threat Vectors Observed by Unit 42 in September 2026." Short. Keep the GLOSSARY open. [KNOWN]
  https://unit42.paloaltonetworks.com/top-5-initial-access-vectors-september-2026/
- Indicators on GitHub: https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel (updated 2026-11-21) [KNOWN]

### Google Threat Intelligence Group and Mandiant

- **What:** long campaign reports on one blog. Mandiant's FLARE team also gives away analysis tools. [KNOWN]
- **How often:** several posts a month. Exact dates are on each article, not the listing. [INFERRED]
- **Level:** advanced. Many posts run 20 to 75 minutes. [KNOWN]
- **Start here:** capa, the FLARE tool that tells you what a program can do (for example "connects to the internet" or "encrypts files"). [KNOWN]
  https://github.com/mandiant/capa
- FLARE-VM sets up a Windows reverse engineering VM: https://github.com/mandiant/flare-vm [KNOWN] Whether it works on Windows for ARM in UTM: [UNKNOWN]. Test before you rely on it.
- Blog: https://cloud.google.com/blog/topics/threat-intelligence

### Kaspersky GReAT (Securelist)

- **What:** APT investigations, ransomware deep dives, and quarterly threat statistics. [KNOWN]
- **How often:** a few posts a week. [INFERRED]
- **Level:** intermediate to advanced. [INFERRED]
- **Start here:** the "Ransomware at the hypervisor layer" post, since you run VMs yourself. [KNOWN that it exists; INFERRED that it fits]
  https://securelist.com/

### ESET Research

- **What:** malware research, with indicators for each investigation on GitHub. [KNOWN]
- **How often:** the IOC repo was updated 2026-11-10. [KNOWN]
- **Level:** intermediate. [INFERRED]
- **Start here:** browse the repo folders. Each one matches a published report. [INFERRED]
  https://github.com/eset/malware-ioc

---

## Offense-side research teams

These find and explain bugs.
Read them for how attackers think.
Never run anything from them outside your lab (SAFETY.md).

### Trail of Bits

- **What:** blog posts on secure code, cryptography, supply chain and AI agents. They also publish a free Testing Handbook and many of their real client security reviews. [KNOWN]
- **How often:** about one post a week. [INFERRED from dates Sep to Nov 2026]
- **Level:** intermediate to advanced. [INFERRED]
- **Lab fit:** Lab 12 (supply chain). Their post "Package managers have an integrity problem" (2026-10-14) fits right in. [KNOWN that it exists]
- **Start here:** the Testing Handbook. It walks through setting up Semgrep, CodeQL and fuzzers. [KNOWN]
  https://appsec.guide/
- Papers, talks and public audit reports: https://github.com/trailofbits/publications [KNOWN]
- Blog: https://blog.trailofbits.com/

### SpecterOps

- **What:** Active Directory and Azure attack research, and open tools, the best known being BloodHound Community Edition. [KNOWN]
- **How often:** one or two posts a week. [INFERRED]
- **Level:** intermediate to advanced. [INFERRED]
- **Start here:** the BloodHound repo. It draws a map of how an attacker could hop from one account to an admin. [KNOWN] It needs a Windows domain lab, which is a big step up for a Mac mini. [INFERRED]
  https://github.com/SpecterOps/BloodHound
- Tool list: https://specterops.io/open-source-tools/
- Blog: https://specterops.io/blog/

### PortSwigger Research

- **What:** new web hacking techniques, from the team that makes Burp Suite. They run a yearly "Top 10 web hacking techniques" list. [KNOWN]
- **How often:** a few posts a month. [INFERRED]
- **Level:** intermediate to advanced. [INFERRED]
- **Lab fit:** Lab 9 (web app testing).
- **Start here:** the Top 10 list. The community nominates research and a panel of experts picks the winners. Lists go back to 2006. [KNOWN]
  https://portswigger.net/research/top-10-web-hacking-techniques

### watchTowr Labs

- **What:** long, funny write-ups of serious bugs in VPNs, firewalls and other edge devices (Citrix, F5, Ivanti and others). [KNOWN]
- **How often:** about two to four posts a month. [INFERRED]
- **Level:** advanced. [INFERRED]
- **Lab fit:** Lab 10. Many of these products show up in CISA KEV. [INFERRED]
- **Start here:** read any one post just for the thinking: how they compare a patched and unpatched version to find the bug. Skip the payload parts. [INFERRED]
  https://labs.watchtowr.com/

### Google Project Zero

- **What:** deep bug research on Windows, Android, Chrome and macOS, plus root cause analyses of zero-days caught being used in the wild. [KNOWN]
- **How often:** about one or two posts a month. [INFERRED from 2026 dates]
- **Level:** advanced. [INFERRED]
- **Start here:** the 0-day Root Cause Analyses list. It has 70 write-ups from 2019 to 2024, all in the same template, so you can compare them. [KNOWN]
  https://googleprojectzero.github.io/0days-in-the-wild/rca.html
- Blog (new address): https://projectzero.google/
- Already in research/README.md (old link).

---

## Mac security

### Objective-See Foundation

- **What:** a non-profit focused on macOS security. Free open-source Mac tools, a blog, a public Mac malware sample collection, and *The Art of Mac Malware* books. [KNOWN]
- **How often:** about one blog post a month, plus a yearly "Mac Malware of the year" roundup. [INFERRED from blog dates]
- **Level:** beginner (tools) to advanced (blog). [INFERRED]
- **Why it matters for you:** it is the only team here built around the same kind of computer you own. [INFERRED]
- **Start here:** install KnockKnock and LuLu on your own Mac. KnockKnock shows what launches at startup. LuLu is a firewall that asks before apps connect out. All their tools are open source. [KNOWN]
  https://objective-see.org/tools.html
- **Then read:** "The Mac Malware of 2025" (posted 2026-01-01). For each sample it covers how it got in, how it stays, and what it does. [KNOWN]
  https://objective-see.org/blog/blog_0x84.html
- **Careful:** that post links to real malware samples. Do not download them. That breaks rule 2 and needs a proper analysis VM. [INFERRED]
- **Book:** the home page says the digital editions are free at taomm.org. [KNOWN] That site did not load for me today. [UNKNOWN] The publisher sells it, with a free sample chapter on persistence. [KNOWN]
  https://nostarch.com/art-mac-malware
- **Free beginner event:** #OFTW, free talks and trainings for students new to Apple security. Whether talks are posted online: [UNKNOWN]
  https://objective-see.org/oftw.html

---

## University research

### Citizen Lab (University of Toronto)

- **What:** investigations into spyware used against journalists and activists, plus censorship and influence operations. [KNOWN]
- **How often:** about one major report a month in fall 2026. [INFERRED from dates]
- **Level:** beginner+ to read. The stories are clear, but the forensics are advanced. [INFERRED]
- **Why read it:** it shows security work that protects real people, not just companies. [INFERRED]
- **Start here:** the October 2026 report on Pegasus spyware attacks on pro-democracy figures in Serbia, linked from the home page. [KNOWN]
  https://citizenlab.ca/
- Their old indicators repo has not been updated since 2020. [KNOWN]
  https://github.com/citizenlab/malware-indicators

For more academic work, research/README.md already links USENIX Security papers and arXiv.

---

## Community projects worth knowing

Not a team, but where a lot of this research ends up.

- **SigmaHQ:** the main shared Sigma rule repo. The DFIR Report sends its rules here. [KNOWN] Pairs with Lab 6.
  https://github.com/SigmaHQ/sigma

---

## Suggested reading plan

1. Every Thursday: one Talos Threat Source issue.
2. After Lab 4: the DFIR Report RDP password spray report.
3. After Lab 6: read 5 Elastic rules and 5 SigmaHQ rules side by side.
4. After Lab 8: the Red Canary Threat Detection Report top 10 techniques.
5. Any time: Objective-See tools on your Mac.
6. Later stretch: one Project Zero root cause analysis a month.

This order is my suggestion. [INFERRED]

---

## Individuals (pending the naming decision in #7)

AGENTS.md rule 4 says to refer to people by role.
Issue #7 will decide whether to allow names for public research.
This section exists so #7 has real examples to judge.

Only public professional work is listed.
No personal details.

- **Patrick Wardle.** Founder of Objective-See and author of *The Art of Mac Malware*. Writes the yearly Mac malware roundup and the free Objective-See tools. [KNOWN]
  https://nostarch.com/art-mac-malware
  https://objective-see.org/blog/blog_0x84.html
- **James Kettle.** Director of Research at PortSwigger. Their team publishes the web hacking research and Top 10 list above. [KNOWN]
  https://portswigger.net/research
- **James Forshaw.** Project Zero researcher. Wrote a 2026 series on bypassing Windows Administrator Protection and how UAC works under the hood. [KNOWN]
  https://projectzero.google/
- **Natalie Silvanovich.** Project Zero researcher. Wrote the 2026 posts on Project Zero's disclosure policy and on how vendors ship emergency fixes. These are readable without deep exploit knowledge. [KNOWN that she wrote them; INFERRED that they are readable]
  https://projectzero.google/
- **Florian Roth.** A listed maintainer of SigmaHQ. Also publishes a large open YARA rule set. [KNOWN]
  https://github.com/SigmaHQ/sigma
  https://github.com/Neo23x0/signature-base
- **Olaf Hartong.** Maintains sysmon-modular, a widely used set of Sysmon logging configs for Windows. [KNOWN]
  https://github.com/olafhartong/sysmon-modular

What #7 might weigh: [INFERRED]

- Names help you find a researcher's other talks and papers.
- These people publish under their own name on purpose.
- The risk is drifting into personal details, which rule 4 is there to stop.

---

## Gaps and open questions

- Red Canary 2026 web report: form or no form? [UNKNOWN]
- taomm.org (free Mac malware books) did not resolve today. [UNKNOWN] Recheck later.
- FLARE-VM on Windows for ARM in UTM. [UNKNOWN]
- I did not add these to `index/entries.csv`. That can happen when the findings get turned into entries. [INFERRED]
- Teams I did not cover: Microsoft Threat Intelligence, NCC Group, Check Point Research, Sophos X-Ops. Worth a later pass.
