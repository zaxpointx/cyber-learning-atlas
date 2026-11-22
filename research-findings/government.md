# Government cyber sources with real hands-on material

Answers issue #3. Checked 2026-11-22.

Every link below was opened for this page.
GitHub stars, last push, license and "archived" come from the GitHub API on 2026-11-22. [KNOWN]

Tags:
[KNOWN] means the source says it.
[INFERRED] means it is my reasoning.
[UNKNOWN] means I looked and did not find it.

Mac fit uses the repo's words:
`arm-ok`, `arm-partial`, `x86-only`, `web`.

---

## The short answer

The best government material is not the big PDFs.
It is a handful of small, working tools and datasets you can open tonight.

- **NIST's macOS Security Compliance Project** is made for your exact machine. [INFERRED]
- **GCHQ's CyberChef** is the best zero-install lab tool any government has ever shipped. [INFERRED]
- **NSA's Ghidra** comes with a free class inside the repo that most people never find. [KNOWN]
- **CISA's ICS parsers** come with sample industrial traffic captures you can feed to Zeek. [KNOWN]
- **DARPA's AIxCC** systems are the most interesting thing to read if you build with AI agents. [INFERRED]

Two warnings:

- CISA's **Logging Made Easy (LME)** was retired on 2026-05-22. Do not build a lab on it. [KNOWN]
- **DARPA's Open Catalog** site (opencatalog.darpa.mil) no longer resolves. It is dead. [KNOWN]

---

## Start here: the top 5

1. **macOS Security Compliance Project** (NIST). Audit your own Mac.
2. **CyberChef** (GCHQ, UK). Decode, decrypt and pick apart data in a browser.
3. **Ghidra + its built-in class** (NSA). Learn reverse engineering.
4. **ICSNPP** (CISA and Idaho National Lab). Read industrial protocols in Zeek.
5. **Attack Flow** (MITRE CTID). Draw a real attack step by step.

Each one is below with a thing to run.

---

## NIST

### 1. macOS Security Compliance Project (mSCP)

- **What:** Security rules for Macs, plus the scripts and profiles that check and apply them. [KNOWN]
- **Who:** NIST, NASA, DISA and Los Alamos staff, plus a community. [KNOWN]
- **Alive:** Yes. 2.5k stars, pushed 2026-11-09. Supports macOS 27. [KNOWN]
- **License:** CC BY 4.0. [KNOWN]
- **Mac fit:** `arm-ok`. It is built for Macs. [KNOWN]
- **You learn:** How a control in NIST SP 800-53 turns into one real setting on a real computer. [INFERRED]
- **Hands-on:** Generate a compliance check script for one baseline. Run it on a **test user account or a macOS VM in UTM**, not your main login. Read every failed rule and decide if you agree. [INFERRED]
- **Gem?** Yes. Almost nobody on the Security+ path knows NIST ships Mac tooling. [INFERRED]
- Links: [repo](https://github.com/usnistgov/macos_security), [site](https://pages.nist.gov/macos_security/)

### 2. SARD and the Juliet test suites

- **What:** A NIST library of over 450,000 small programs with known security bugs, sorted by CWE. [KNOWN]
- **Alive:** The site is up and downloads need no login. No dates are shown. [KNOWN] Juliet 1.3 is the current suite. [KNOWN]
- **License:** [UNKNOWN] Not shown on the pages I opened.
- **Mac fit:** `arm-ok`. They are source files. [INFERRED]
- **You learn:** What a buffer overflow or SQL injection looks like in code, and how scanners find (or miss) it. [INFERRED]
- **Hands-on:** Download Juliet C/C++ 1.3. Pick one CWE folder (try CWE-121, stack overflow). Run a free scanner like cppcheck on it. Count how many bugs it catches. [INFERRED]
- **Gem?** Yes. It is a free answer key for testing code scanners. [INFERRED]
- Links: [SARD](https://samate.nist.gov/SARD/), [test suites](https://samate.nist.gov/SARD/test-suites)

### 3. NCCoE practice guides (SP 1800 series)

- **What:** Guides where NIST and vendors actually build a setup and write down how. [KNOWN]
- **Best one now:** SP 1800-35, Zero Trust. Final June 2025. 19 example builds with 24 collaborators. [KNOWN]
- **Older but fun:** SP 1800-15, home and small business IoT protection with MUD. Final May 2021. [KNOWN]
- **License:** NIST publication, free to read. [KNOWN]
- **Mac fit:** `web` (reading). [INFERRED]
- **Honest note:** Most builds use paid vendor products. You cannot rebuild them at home as written. [INFERRED]
- **Hands-on:** Read the SP 1800-35 summary. Then draw your own lab as a mini zero trust design: who can talk to what, and what checks each step. [INFERRED]
- Note: the nccoe.nist.gov site blocked my automated reader. The CSRC pages below opened fine. [KNOWN]
- Links: [SP 1800-35](https://csrc.nist.gov/pubs/sp/1800/35/final), [SP 1800-15](https://csrc.nist.gov/pubs/sp/1800/15/final)

### Also from NIST (honorable mentions)

- **OSCAL:** Security controls written as machine-readable data. 975 stars, pushed 2026-11-16. Good later, if you like data formats. [KNOWN] [repo](https://github.com/usnistgov/OSCAL)
- **Dioptra:** A NIST test platform for checking AI systems. Release 1.2.3. Pushed 2026-11-19. Interesting for an AI builder, but heavy. [KNOWN] [repo](https://github.com/usnistgov/dioptra)

---

## NSA

### 4. Ghidra, with its hidden class

- **What:** NSA's free reverse engineering tool. You open a program and read what it really does. [KNOWN]
- **Alive:** Very. 101k stars. Release 12.2 on 2026-10-22. [KNOWN]
- **License:** Apache-2.0. [KNOWN]
- **Mac fit:** `arm-partial`. Runs on macOS ARM, but you must build the small native parts yourself once. Needs JDK 25 and 4 GB RAM. [KNOWN]
- **You learn:** How compiled programs work under the hood. Assembly, functions, strings. [INFERRED]
- **The gem:** The repo has a full course in `GhidraDocs/GhidraClass`. Beginner, Intermediate and Advanced folders, a student guide, and exercise files. [KNOWN]
- **Hands-on:** Compile a tiny C "hello world" on your Mac. Open it in Ghidra. Find `main` and rename every variable. Then work through the Beginner student guide. [INFERRED]
- Links: [repo](https://github.com/NationalSecurityAgency/ghidra), [class folder](https://github.com/NationalSecurityAgency/ghidra/tree/master/GhidraDocs/GhidraClass), [getting started](https://github.com/NationalSecurityAgency/ghidra/blob/master/GhidraDocs/GettingStarted.md)

### 5. ELITEWOLF

- **What:** NSA's Snort alert rules for industrial gear (Siemens, Rockwell, SEL). [KNOWN]
- **Alive:** Quiet. Last push 2024-01-07. Rules are text, so they still teach. [KNOWN]
- **License:** Public domain (US government work, CC0). [KNOWN]
- **Mac fit:** `arm-ok`. Text rules. [INFERRED]
- **You learn:** What "normal but worth checking" looks like on an industrial network. NSA warns hits are not always bad. [KNOWN]
- **Hands-on:** Read the Siemens rule file. Pair it with the S7comm sample captures from ICSNPP (find 6). Convert one rule idea into a Suricata rule. [INFERRED]
- **Gem?** Yes. Ties straight into ORNL style grid and OT work. [INFERRED]
- Link: [repo](https://github.com/nsacyber/ELITEWOLF)

### Also from NSA

- **nsacyber guidance repos** (AppLocker, event forwarding, web shells, firmware). Useful reading, mostly old. AppLocker guidance was the latest touched, 2025-10-31. [KNOWN] [org](https://github.com/nsacyber)
- **WALKOFF** automation is archived. Skip. [KNOWN]

---

## CISA

### 6. ICSNPP (industrial protocol parsers for Zeek)

- **What:** Add-ons that teach Zeek to read industrial protocols like BACnet, S7comm, Modbus, DNP3 and OPC UA. Built by Idaho National Lab for CISA. [KNOWN]
- **Alive:** Yes. Pushed 2026-11-10. [KNOWN]
- **License:** BSD-3-Clause. [KNOWN]
- **Mac fit:** `arm-ok` in a Linux VM with Zeek. Zeek has arm64 images (see tools/README). The plugins build from source. [INFERRED]
- **You learn:** How factories and power systems talk, and what a defender can log. [INFERRED]
- **The gem:** Each parser repo ships sample `.pcap` captures in `testing/traces`. For example `s7comm_plus.pcap` and `modbus_example.pcap`. [KNOWN]
- **Hands-on:** In your Zeek VM, install one parser. Run Zeek on its sample pcap. Open the new log and explain each column. [INFERRED]
- Links: [ICSNPP](https://github.com/cisagov/ICSNPP), [S7comm parser](https://github.com/cisagov/icsnpp-s7comm)

### 7. Malcolm

- **What:** A full network analysis kit (Zeek, Suricata, Arkime, OpenSearch dashboards) in one package. [KNOWN]
- **Alive:** Very. Release v26.10.0 on 2026-10-29. [KNOWN]
- **License:** Apache-2.0 (per README). [KNOWN]
- **Mac fit:** `arm-partial`. It publishes arm64 images and runs on Apple silicon with Docker Desktop. But it wants 8 cores and **24 GB of RAM** minimum. [KNOWN] A Mac mini may not have that to spare. [INFERRED]
- **You learn:** What a real SOC network sensor stack looks like when it is all wired together. [INFERRED]
- **Hands-on:** Only if you have the RAM. Load a sample pcap (like the ICSNPP ones) and explore the dashboards. Otherwise stay with plain Zeek + Suricata. [INFERRED]
- **Gem?** Yes. It is the Apple silicon answer to Security Onion, which is x86 only. [INFERRED]
- Links: [repo](https://github.com/cisagov/Malcolm), [macOS notes](https://github.com/cisagov/Malcolm/blob/main/docs/host-config-macos.md)

### 8. Decider

- **What:** A web app that walks you through mapping what an attacker did to ATT&CK, by asking questions. [KNOWN]
- **Alive:** Yes. Version 3.0 is login-less. Pushed 2026-02-20. [KNOWN]
- **License:** CC BY 4.0. [KNOWN]
- **Mac fit:** `arm-ok` via Docker. The README has M1 setup notes. [KNOWN]
- **You learn:** How analysts turn a story ("they stole passwords") into technique IDs. [INFERRED]
- **Hands-on:** Take one incident from this repo's `incidents/` folder. Map three behaviors with Decider. Compare to the IDs we already list. [INFERRED]
- Link: [repo](https://github.com/cisagov/decider)

### 9. Eviction Strategies Tool (Playbook-NG)

- **What:** Turns observed attacker techniques into a cleanup plan. Has ready templates, like ransomware. [KNOWN]
- **Alive:** Yes. Pushed 2026-11-02. Loaded with ATT&CK Enterprise 20.0. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `web`. CISA hosts a live copy. You can also run it yourself with Node. [KNOWN]
- **You learn:** The step after detection: how you actually kick an attacker out. [INFERRED]
- **Hands-on:** Open the ransomware template. Pick the five countermeasures you could do in your own lab. Write why. [INFERRED]
- **Gem?** Yes. CISA says it is good for building tabletop exercises. [KNOWN]
- Links: [live tool](https://www.cisa.gov/eviction-strategies-tool), [repo](https://github.com/cisagov/playbook-ng)

### 10. Vulnrichment

- **What:** CISA's extra notes on new CVEs: SSVC decision points, a KEV flag, and sometimes CWE and CVSS. [KNOWN]
- **Alive:** Yes. Pushed today, 2026-11-22. [KNOWN]
- **License:** CC0-1.0. [KNOWN]
- **Mac fit:** `arm-ok`. JSON files. [KNOWN]
- **You learn:** How CISA decides which bugs matter. Pairs with SSVC (find 13) and `scripts/kev_lookup.py`. [INFERRED]
- **Hands-on:** Pick five CVEs from this month. Read each file's SSVC block. Sort them into "fix now" and "fix later" and check yourself against CISA. [INFERRED]
- Link: [repo](https://github.com/cisagov/vulnrichment)

### Also from CISA

- **Thorium:** File analysis platform from Sandia and CISA. BSD-3. Pushed 2026-11-16. Has a single-node install. Heavy, and arm support is [UNKNOWN]. [KNOWN] [repo](https://github.com/cisagov/thorium)
- **ScubaGear and Untitled Goose Tool:** Real and alive, but need a Microsoft 365 or Azure tenant you control. Skip for now. [KNOWN] [ScubaGear](https://github.com/cisagov/ScubaGear), [Goose](https://github.com/cisagov/untitledgoosetool)
- **Archived, skip:** LME (retired 2026-05-22), RedEye, CHIRP, Sparrow. [KNOWN] [LME notice](https://github.com/cisagov/LME)

---

## DARPA

### 11. AIxCC: the open AI bug-finding systems

- **What:** In DARPA's AI Cyber Challenge, teams built systems that find and patch bugs in open source code on their own. [KNOWN]
- **Results:** Team Atlanta won, Trail of Bits second, Theori third. Systems found 54 planted bugs and patched 43. [KNOWN]
- **Open:** All seven finalist systems were promised as OSI open source. Repos are linked from the archive. [KNOWN]
- **Mac fit:** Mostly `x86-only` or Linux-cluster scale for the competition versions. [INFERRED]
- **You learn:** How fuzzing, code analysis and LLM agents are wired into one pipeline. Great reading for an agent builder. [INFERRED]
- **Hands-on:** Do not run the full systems. Read one system's design doc and draw its pipeline as boxes and arrows. [INFERRED]
- Links: [DARPA results](https://darpa.mil/news/2025/aixcc-results), [archive with all repos](https://archive.aicyberchallenge.com/)

Finalist repos (final round), checked on GitHub:

| System | Team | License | Last push |
|---|---|---|---|
| [Atlantis](https://github.com/Team-Atlanta/aixcc-afc-atlantis) | Team Atlanta | not stated by GitHub | 2025-11-25 |
| [Buttercup (final)](https://github.com/trailofbits/afc-buttercup) | Trail of Bits | AGPL-3.0, archived | 2025-07-14 |
| [RoboDuck](https://github.com/theori-io/aixcc-afc-archive) | Theori | AGPL-3.0, archived | 2025-08-05 |
| [Artiphishell](https://github.com/shellphish/artiphishell) | Shellphish | MIT | 2025-08-27 |
| [Fuzzing Brain](https://github.com/o2lab/afc-crs-all-you-need-is-a-fuzzing-brain) | All You Need Is A Fuzzing Brain | Apache-2.0 | 2026-11-17 |
| [Bug Buster](https://github.com/42-b3yond-6ug/42-b3yond-6ug-crs) | 42 b3yond 6ug | GPL-3.0 | 2025-08-19 |
| [Lacrosse](https://github.com/siftech/afc-crs-lacrosse) | Lacrosse | MIT | 2025-08-24 |

### 12. Buttercup (standalone) and SHERPA

- **Buttercup standalone** is the cleaned-up version you can run on one machine. [KNOWN]
  - Alive: 1.8k stars, pushed 2026-11-02. AGPL-3.0. [KNOWN]
  - Mac fit: `arm-partial`. macOS works via Docker Desktop or Colima. ARM64 support is partial. [KNOWN]
  - Needs 8 cores, 16 GB RAM, 100 GB disk, **and paid LLM API keys**. [KNOWN] Set its budget limit. Ask before spending money. [INFERRED]
  - Hands-on: Run it against its own practice target (an example libpng challenge) only. [KNOWN] Never against code you do not own or a live site.
- **SHERPA** writes fuzzing harnesses with AI. MIT. Pushed 2026-01-23. On Apple silicon it tells you to force amd64 Docker, so it runs slowly under emulation. [KNOWN]
- Links: [Buttercup](https://github.com/trailofbits/buttercup), [SHERPA](https://github.com/AIxCyberChallenge/sherpa)

### DARPA Open Catalog: dead

- The old index of DARPA open software (opencatalog.darpa.mil) did not resolve on 2026-11-22. [KNOWN]
- Only 2014 era news and web archives point to it. Treat it as history. [INFERRED]
- Link: [2014 DARPA announcement](https://www.darpa.mil/news/2014/open-catalog)

---

## CERT/CC and CMU SEI

### 13. SSVC (vulnerability decisions)

- **What:** A decision tree for "how fast should we fix this bug?" CISA uses it. [KNOWN]
- **Alive:** Yes. Pushed 2026-11-21. [KNOWN]
- **License:** Mixed by folder (see repo). Built under DHS funding at CMU. [KNOWN]
- **Mac fit:** `web`. The docs site has a Calculator and an Explorer. [KNOWN]
- **You learn:** Why "CVSS 9.8" alone is not a plan. [INFERRED]
- **Hands-on:** Run three KEV entries through the SSVC Calculator. Then compare with CISA's answer in Vulnrichment (find 10). [INFERRED]
- Links: [docs and calculator](https://certcc.github.io/SSVC/), [repo](https://github.com/CERTCC/SSVC)

### 14. Kaiju (Ghidra add-on)

- **What:** CERT's tools for Ghidra, like function hashing to spot reused code in malware. [KNOWN]
- **Alive:** Yes. Pushed 2026-10-23. [KNOWN]
- **License:** BSD-style. [KNOWN]
- **Mac fit:** `arm-partial`. Same as Ghidra. [INFERRED]
- **You learn:** How analysts tell two programs share code. [INFERRED]
- **Hands-on:** After the Ghidra class, install Kaiju. Hash functions in two versions of your own small program and see what matches. [INFERRED]
- Link: [repo](https://github.com/CERTCC/kaiju)

### 15. GHOSTS (fake users for your lab)

- **What:** Simulates people using computers: browsing, typing documents, sending traffic. Made for cyber exercises. [KNOWN]
- **Alive:** Yes. Version 9, pushed 2026-11-20. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-partial`. The Universal client runs on Windows, Linux and macOS with .NET. Docker image arm support [UNKNOWN]. [KNOWN]
- **You learn:** Why real networks are noisy, and how hard it is to spot an attacker in the noise. [INFERRED]
- **Hands-on:** Run one GHOSTS client in a lab VM for an hour. Then look at what Zeek logged. Can you tell the fake human from a scan? [INFERRED]
- **Gem?** Yes. It makes a home lab feel like a real office. [INFERRED]
- Links: [repo](https://github.com/cmu-sei/GHOSTS), [docs](https://cmu-sei.github.io/GHOSTS/)

### 16. SiLK and YAF (network flow tools)

- **What:** CERT's NetSA suite for flow records (who talked to whom, how much). SiLK 3.24.2, YAF 2.20.3. [KNOWN]
- **Alive:** Versions are current-looking, but the page shows no dates. [KNOWN] [UNKNOWN] on release dates.
- **License:** [UNKNOWN] Not on the main page.
- **Mac fit:** [UNKNOWN] Offered as RPMs for Red Hat style Linux. [KNOWN]
- **You learn:** Flow analysis, which is how big networks are watched when full packets are too much. [INFERRED]
- **Hands-on:** Later, after Zeek. Compare a SiLK flow view to Zeek's `conn.log` on the same pcap. [INFERRED]
- Link: [NetSA tools](https://tools.netsa.cert.org/)

### Also from SEI

- **Pharos:** Only supports 32-bit x86 Windows programs. Use Kaiju instead. [KNOWN] [repo](https://github.com/cmu-sei/pharos)
- **Crucible and TopoMojo:** SEI's cyber range builders. Alive, but built for big servers. Good reading on how ranges work. [INFERRED] [Crucible](https://github.com/cmu-sei/crucible)

---

## MITRE Center for Threat-Informed Defense (CTID)

Note: Caldera, ATT&CK and D3FEND are already in this repo. These are the others.

### 17. Attack Flow

- **What:** A way to draw an attack as a chain of steps, plus a builder. Now version 4.0. [KNOWN]
- **Alive:** Yes. Pushed 2026-11-16. [KNOWN]
- **License:** Apache-2.0. [KNOWN]
- **Mac fit:** `web`. The builder is hosted on GitHub Pages. [KNOWN]
- **You learn:** That attacks are sequences, not single techniques. [INFERRED]
- **Hands-on:** Pick one incident in this repo. Draw it in the Attack Flow builder, five to ten steps. Save the file next to your write-up. [INFERRED]
- Links: [site](https://center-for-threat-informed-defense.github.io/attack-flow/), [builder](https://center-for-threat-informed-defense.github.io/attack-flow/ui/), [repo](https://github.com/center-for-threat-informed-defense/attack-flow)

### 18. Summiting the Pyramid

- **What:** Research on writing detections that are hard for attackers to dodge. Updated September 2026. [KNOWN]
- **Alive:** Yes. Pushed 2026-09-29. [KNOWN]
- **License:** Apache-2.0. [KNOWN]
- **Mac fit:** `web` (docs). [KNOWN]
- **You learn:** Why matching a file name is weak and matching behavior is strong. [INFERRED]
- **Hands-on:** Take your Lab 6 Sigma rule. Score it with their method. Rewrite it to sit one level higher. [INFERRED]
- **Gem?** Yes. This is the best next step after writing your first Sigma rules. [INFERRED]
- Links: [site](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/), [repo](https://github.com/center-for-threat-informed-defense/summiting-the-pyramid)

### 19. Top ATT&CK Techniques

- **What:** A ranked list of the techniques to defend first, with a calculator you can tune. [KNOWN]
- **Alive:** Yes. Pushed 2026-11-20. Apache-2.0. [KNOWN]
- **Mac fit:** `web`. [KNOWN]
- **Hands-on:** Run the calculator for a small network like yours. Check which top techniques your labs already cover. [INFERRED]
- Links: [site](https://center-for-threat-informed-defense.github.io/top-attack-techniques/), [repo](https://github.com/center-for-threat-informed-defense/top-attack-techniques)

### 20. Adversary Emulation Library

- **What:** Full step-by-step plans that copy real threat groups, plus small "micro" plans for single behaviors. [KNOWN]
- **Alive:** Slowing. Last push 2025-05-28. [KNOWN]
- **License:** Apache-2.0. [KNOWN]
- **Mac fit:** `arm-partial`. Most micro plans target Windows (registry, DLL sideloading, named pipes). [KNOWN]
- **Safety:** These run real attacker behavior. Only in a snapshotted, isolated lab VM. Read each plan first. Do not copy its code into this repo. [INFERRED]
- **Hands-on:** Start by just reading one plan's intelligence summary and emulation steps. Map each step to ATT&CK. [INFERRED]
- Link: [repo](https://github.com/center-for-threat-informed-defense/adversary_emulation_library)

### Also from CTID

- **Mappings Explorer:** Shows which security controls cover which ATT&CK techniques. Pushed 2026-11-18. `web`. [KNOWN] [site](https://ctid.mitre.org/mappings/)
- **Newest projects:** CIS Controls for Threat Mitigations (Oct 2026) and Secure AI with MITRE ATLAS (May 2026). [KNOWN] [projects](https://ctid.mitre.org/projects/)

---

## Allied governments

### 21. CyberChef (GCHQ, UK)

- **What:** "The Cyber Swiss Army Knife." Chain small steps to decode, decrypt, unzip and analyze data. [KNOWN]
- **Alive:** Very. 36.5k stars. Build compiled 2026-11-20. [KNOWN]
- **License:** Apache-2.0. [KNOWN]
- **Mac fit:** `web`. Runs fully in your browser. Only three operations call out to the internet. [KNOWN]
- **You learn:** Base64, hex, XOR, hashing, timestamps. All Security+ words, made touchable. [INFERRED]
- **Hands-on:** Base64 encode a sentence, then XOR it with a key, then reverse both steps. Save the recipe. [INFERRED]
- **Gem?** The best one here. Works in five seconds. [INFERRED]
- Links: [live app](https://gchq.github.io/CyberChef/), [repo](https://github.com/gchq/CyberChef)

### 22. Assemblyline 4 (Canadian Centre for Cyber Security)

- **What:** An automated file triage and malware analysis platform. [KNOWN]
- **Alive:** Yes. Pushed 2026-11-20. MIT. [KNOWN]
- **Mac fit:** [UNKNOWN] for arm64. Docs list Ubuntu 22.04/24.04 and RHEL, minimum 4 CPUs and 8 GB RAM. [KNOWN]
- **You learn:** How a national CERT scans millions of files a day. [KNOWN] [INFERRED]
- **Hands-on:** Later. If it runs in your ARM Ubuntu VM, submit only the harmless EICAR test file and read the report. [INFERRED]
- Links: [repo](https://github.com/CybercentreCanada/assemblyline), [Docker install docs](https://cybercentrecanada.github.io/assemblyline4_docs/installation/appliance/docker/)

### Skipped allied items

- **UK NCSC Exercise in a Box:** Free, but I could not confirm it works without an account. [UNKNOWN] Left out under the no sign-up rule.
- **NCSC-NL repos:** Mostly scanners for specific old CVEs. Too narrow to learn from. [INFERRED]

---

## What is new versus this repo

Already in the repo (not repeated as new):
- Caldera, ATT&CK, D3FEND, ATT&CK STIX data, CISA KEV data. [KNOWN]
- NIST CSF, SP 800-61, 800-115, 800-63, 800-53, 800-82. [KNOWN]
- CISA advisories, Cyber Essentials, Secure by Design. [KNOWN]

New from this ticket:
- Tools: mSCP, CyberChef, Ghidra (+ class), Kaiju, ELITEWOLF, ICSNPP, Malcolm, Decider, Eviction Strategies Tool, GHOSTS, SiLK/YAF, Assemblyline, Buttercup.
- Data: SARD/Juliet, Vulnrichment.
- Methods (web): SSVC, Attack Flow, Summiting the Pyramid, Top ATT&CK Techniques, Mappings Explorer.
- Research to read: NCCoE SP 1800-35 and 1800-15, AIxCC finalist systems.
- Warnings: LME retired, DARPA Open Catalog dead.

None of these were added to `index/entries.csv` yet. That is a follow-up step. [KNOWN]

---

## Best 5 for a deep "project reading"

1. **AIxCC Buttercup** (standalone). A full AI bug-finder you can actually read end to end.
2. **Ghidra's GhidraClass folder.** A real course hiding in a repo.
3. **mSCP.** How a rule goes from a NIST PDF to a script on your Mac.
4. **Malcolm.** How a full sensor stack is wired together.
5. **Summiting the Pyramid.** How to write detections that last.

---

## Rules check

- Public pages only. No logins, no sign-up walls. [KNOWN]
- Nothing opened was marked CUI, OUO, FOUO or export controlled. [KNOWN]
- No exploit code copied. Emulation and AIxCC repos are linked, not copied. [KNOWN]
- People are named by role only. [KNOWN]
- No affiliation with any agency or MITRE is claimed. [KNOWN]
