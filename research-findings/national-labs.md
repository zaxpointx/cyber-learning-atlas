# National labs: open cyber projects you can learn from

Question (issue #2): which national labs, besides ORNL and Y-12, publish open cybersecurity projects a student can actually run and learn from?

Checked: 2026-11-22.

## The short answer

- **INL is the clear winner.** It ships the most, and the most usable: Malcolm, the ICSNPP Zeek parsers, CSET, CyOTE Insights. [KNOWN]
- **LLNL is second, and the best for reverse engineering.** Ghidra 101, OGhidra, Surfactant, EyeON, Wintap. [KNOWN]
- **Sandia is the cyber range lab.** minimega and FIREWHEEL build whole fake networks. But they want x86 Linux with KVM, so they fight your Mac. [INFERRED]
- **LBNL gave the world Zeek** (it started there as Bro). Its own cyber org is small and mostly old. [KNOWN]
- **PNNL and LANL are data plus ML.** LANL's big gift is its de-identified network datasets. [KNOWN]
- **Argonne, NREL and Brookhaven publish little you can run.** Argonne runs the CyberForce competition. NREL lists tools in DOE CODE but rarely posts the code. Brookhaven: nothing found. [INFERRED]

## How to read this page

Each find has the same short card.

- **Alive** means last real commit or release.
- **Mac fit** uses the repo's labels:
  - `arm-ok`: runs on Apple Silicon (native or in an ARM Linux VM)
  - `arm-partial`: some parts run, some need x86
  - `x86-only`: needs an Intel/AMD machine in practice
  - `web`: runs in a browser
- Tags: [KNOWN] is in the source. [INFERRED] is my reasoning. [UNKNOWN] means I looked and did not find it.

A note on INL "alive" dates. In June 2026 INL archived dozens of repos and added an archival notice commit to each one (2026-06-18). That date is not real work. I list the last real commit before it. [KNOWN]

---

## Start here: top 5 for a deep "project reading"

1. **ICSNPP + Zeek** (INL, via CISA). Smallest, cleanest way into ICS traffic. Plugs into your Lab 5 sensor.
2. **Ghidra 101** (LLNL). Real intern training materials with practice binaries.
3. **Malcolm** (INL, via CISA). A full network analysis stack. Heavy, but the docs are a course in themselves.
4. **Surfactant** (LLNL). SBOMs from real files. Pairs with Lab 12.
5. **LANL cyber datasets.** Real (de-identified) enterprise logs with red team events marked.

Why these five: all are alive or stable, all run on your Mac, and each teaches a skill that shows up on Security+ or in a SOC job. [INFERRED]

---

## Idaho National Laboratory (INL)

INL publishes under `idaholab`, `IdahoLabResearch`, `IdahoLabUnsupported`, and many cyber tools under `cisagov` (built by INL for CISA). [KNOWN]

### Malcolm

- **What:** a network traffic analysis suite. Feed it PCAP files, Zeek logs or Suricata alerts. It gives you OpenSearch dashboards and Arkime session search. [KNOWN]
- **Alive:** yes. Release v26.10.0 on 2026-10-29. [KNOWN]
- **License:** Apache 2.0 (per README). [KNOWN]
- **Mac fit:** `arm-ok`, but heavy. Publishes ARM64 images for Apple Silicon. Wants 24 GB RAM minimum, 32 GB recommended. [KNOWN]
- **You learn:** how a SOC turns raw packets into searchable sessions and dashboards.
- **Try this:** if your Mac mini has 24 GB or more, run it in Docker and load a sample PCAP. If not, skip Malcolm and use ICSNPP plus plain Zeek (below). [INFERRED]
- **Sources:** [repo](https://github.com/cisagov/Malcolm), [macOS host notes](https://github.com/cisagov/Malcolm/blob/main/docs/host-config-macos.md), [system requirements](https://github.com/cisagov/Malcolm/blob/main/docs/system-requirements.md)

### ICSNPP (Industrial Control Systems Network Protocol Parsers)

- **What:** Zeek plugins that read ICS protocols: Modbus, DNP3, BACnet, S7comm, OPC UA, EtherNet/IP and more. [KNOWN]
- **Alive:** yes. Parsers updated through Oct and Nov 2026. icsnpp-modbus v2.0.0 released 2025-09-03. [KNOWN]
- **License:** BSD 3-Clause. [KNOWN]
- **Mac fit:** `arm-ok`. Zeek has Homebrew builds for Apple Silicon. The parsers install with Zeek's package manager. [KNOWN] for Zeek, [INFERRED] for each parser.
- **You learn:** what "OT traffic" looks like, and how a sensor decodes a protocol into logs.
- **Try this:** `zkg install icsnpp-modbus`, then run Zeek on the sample `modbus_example.pcap` that ships in the repo. Read the new `modbus_*.log` files. [KNOWN] (steps are in the README)
- **Lesser-known angle:** each parser repo is a small, readable example of how to write a Zeek protocol parser. [INFERRED]
- **Sources:** [ICSNPP index](https://github.com/cisagov/ICSNPP), [icsnpp-modbus](https://github.com/cisagov/icsnpp-modbus), [DOE CODE record](https://www.osti.gov/doecode/biblio/49859), [Zeek Homebrew formula](https://formulae.brew.sh/formula/zeek)

### CSET (Cyber Security Evaluation Tool)

- **What:** a guided self-assessment. You describe a site, it compares you to security standards and gives recommendations. Built by CISA and INL. [KNOWN]
- **Alive:** yes. v13.0.0.0 released 2026-10-06. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-partial`. The installer is Windows only. Mac users are told to use Docker. Whether every container has an ARM64 image is [UNKNOWN].
- **You learn:** the "governance and compliance" side of Security+. How auditors turn a standard into questions.
- **Try this:** run it in Docker and assess your own home lab as if it were a tiny business. [INFERRED]
- **Sources:** [repo](https://github.com/cisagov/cset)

### CyOTE Insights (gem)

- **What:** a desktop dashboard of historical OT cyber attacks. Compare incidents, trends and costs. [KNOWN]
- **Alive:** yes. v1.0.0 released 2026-06-24. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-ok`. Ships a macOS installer labeled Apple Silicon. Runs offline. [KNOWN]
- **You learn:** the real history of ICS attacks. A good companion to the `incidents/` folder (Ukraine grid 2015, Volt Typhoon).
- **Try this:** install it, pick one OT incident, and write a one-page timeline. [INFERRED]
- **Sources:** [repo](https://github.com/idaholab/Insights)

### CIE Engineered Controls Database (gem)

- **What:** a catalog of "engineered controls" across all 18 critical infrastructure sectors, with a browser dashboard. Part of INL's Cyber-Informed Engineering work. [KNOWN]
- **Alive:** last commit 2026-06-01. [KNOWN]
- **License:** none listed on GitHub. [KNOWN] Treat it as read-only reference. [INFERRED]
- **Mac fit:** `web`. A standalone HTML dashboard, no install. [KNOWN]
- **You learn:** the big idea that physics and engineering can stop an attack that software alone cannot (for example, a mechanical relief valve). [INFERRED]
- **Sources:** [repo](https://github.com/idaholab/CIE_EC_Database)

### 5GAD-2022 dataset (gem)

- **What:** packet captures of normal traffic and attacks against a lab 5G core (free5GC). Made for training attack detectors. [KNOWN]
- **Alive:** archived. Last real commit 2024-10-31. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-ok`. It is just PCAP files. Open in Wireshark. Needs git-lfs to clone. [KNOWN]
- **You learn:** Wireshark filtering on a protocol most people never see.
- **Try this:** the README walks you through splitting traffic by interface in Wireshark. Do that, then compare a normal capture to an attack capture. [KNOWN]
- **Sources:** [repo](https://github.com/IdahoLabResearch/5GAD)

### Living-off-the-land anomaly detection

- **What:** reads Zeek logs, builds a graph of who talks to whom, and flags connections that break the normal structure. [KNOWN]
- **Alive:** archived. Last real commit 2025-12-16. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-ok`. Python. [INFERRED]
- **You learn:** why "normal" network structure matters for spotting attackers who use built-in tools.
- **Try this:** read the README's model breakdown. Then feed it Zeek `conn.log` from your own lab. [INFERRED]
- **Sources:** [repo](https://github.com/IdahoLabUnsupported/lotl-network-anomaly-detection), [DOE CODE search hit](https://www.osti.gov/doecode/biblio/168028)

### Also from INL (quick notes)

- **Buggy Program Program:** generates random C programs with known bug classes. Archived, last real commit 2022-10. Great for bug-hunting practice, but the README is now only an archival notice. [KNOWN] [repo](https://github.com/IdahoLabResearch/Buggy-Program-Program)
- **AcCCS:** EV charging (CCS) communication emulators. Needs special hardware. [KNOWN] [repo](https://github.com/IdahoLabResearch/AcCCS)
- **cape2stix, ATIS:** convert malware and threat data into STIX. Archived. [KNOWN] [cape2stix](https://github.com/idaholab/cape2stix)

---

## Lawrence Livermore National Laboratory (LLNL)

GitHub org: `llnl`. Lots of HPC code, plus a strong cluster of cyber tools. [KNOWN]

### Ghidra 101 (gem)

- **What:** tutorials, practice binaries and challenges used to teach Ghidra to LLNL's Cybersecurity Summer Institute students. [KNOWN]
- **Alive:** last commit 2026-02-06. [KNOWN]
- **License:** BSD 3-Clause with a commercial license alternative. [KNOWN]
- **Mac fit:** `arm-ok`. Ghidra runs on Apple Silicon. Some practice binaries may be x86, which Ghidra can still read. [INFERRED]
- **You learn:** reverse engineering basics: finding a password check, reading a disassembly.
- **Try this:** start with the `csi2022-ghidra-tutorial` folder. Compile the example, load it in Ghidra, and find the password check. [INFERRED]
- **Heads up:** one folder is called `hmi-backdoor`. It is a training challenge, not malware. Still, open it only in your lab VM. [INFERRED]
- **Sources:** [repo](https://github.com/llnl/ghidra-101), [DOE CODE record](https://www.osti.gov/doecode/biblio/176202), [CSI program page](https://cyber-internship.llnl.gov/)

### OGhidra

- **What:** connects Ghidra to an AI model (local via Ollama, or cloud) so you can ask questions about a binary in plain English. [KNOWN]
- **Alive:** very. Last commit 2026-11-18. About 470 stars. [KNOWN]
- **License:** BSD 3-Clause with commercial alternative. [KNOWN]
- **Mac fit:** `arm-ok`. Python, Java 21, Ghidra, Ollama all run on Apple Silicon. [INFERRED]
- **You learn:** how analysts speed up reverse engineering, and where AI gets it wrong.
- **Try this:** do one Ghidra 101 challenge by hand first. Then ask OGhidra the same question and compare. [INFERRED]
- **Sources:** [repo](https://github.com/llnl/OGhidra)

### Surfactant

- **What:** scans a folder of files (EXE, ELF, MSI and more) and builds a Software Bill of Materials (SBOM). [KNOWN]
- **Alive:** yes. Last commit 2026-11-21. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-ok`. Installs with `pip`. Mac Mach-O support is an optional extra. [KNOWN]
- **You learn:** supply chain security. What is actually inside the software you run.
- **Try this:** run it on a folder of tools in your Linux VM. Open the SBOM and find every library. Fits Lab 12. [INFERRED]
- **Sources:** [repo](https://github.com/llnl/Surfactant)

### EyeON (pEyeON)

- **What:** a command line tool that makes a manifest of installed software and firmware, for threat and inventory work. [KNOWN]
- **Alive:** yes. Last push 2026-11-16. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-ok`. Its container image is multi-arch (amd64 and arm64). [KNOWN]
- **You learn:** asset inventory, the first step of every security program.
- **Sources:** [repo](https://github.com/llnl/pEyeON)

### Wintap

- **What:** a Windows agent that collects host events (ETW and more) into one data model, with a local web "workbench" to query them. [KNOWN]
- **Alive:** release v6.1.0.4 in 2024-10. Last commit 2025-03. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `x86-only` in practice. Needs Windows 10 x64 and .NET 4.8. [KNOWN] It might run in Windows 11 ARM in UTM under emulation. [UNKNOWN]
- **You learn:** endpoint telemetry. Compare to Wazuh and osquery in Lab 7.
- **Note:** `Wintap-Data` was meant to hold sample data but contains only a license file. Lintap (a Linux version) is an early proof of concept. [KNOWN]
- **Sources:** [repo](https://github.com/llnl/Wintap), [Lintap](https://github.com/llnl/Lintap)

---

## Sandia National Laboratories

GitHub orgs: `sandialabs` (about 870 repos) and `sandia-minimega`. [KNOWN]

### minimega

- **What:** launches and manages lots of virtual machines fast, from one laptop up to a cluster. The engine under Sandia's cyber ranges. [KNOWN]
- **Alive:** yes. Release 3.3.0 on 2026-09-22. [KNOWN]
- **License:** GPL-3.0. [KNOWN]
- **Mac fit:** `x86-only` in practice. Released packages are amd64 only. It needs KVM, which means a Linux host with hardware virtualization. [KNOWN] for the packages, [INFERRED] for the rest.
- **You learn:** how cyber ranges are built. The free **Mini101** course is the real treasure here. [KNOWN]
- **Try this:** read Mini101 module 1 even if you cannot run it yet. It explains VM networking clearly. [INFERRED]
- **Sources:** [repo](https://github.com/sandia-minimega/minimega), [docs and Mini101](https://sandia-minimega.github.io/minimega/), [Sandia page](https://www.sandia.gov/minimega/)

### FIREWHEEL and phenix

- **What:** FIREWHEEL builds repeatable network experiments from "model components" (DNS, NTP, VyOS routers, Windows, Linux). phenix is a GUI that orchestrates minimega. [KNOWN]
- **Alive:** both very active. FIREWHEEL v3.1.0 (2026-10-22). phenix release 2026-11-12. [KNOWN]
- **License:** FIREWHEEL core unclear on GitHub (model components are Apache 2.0). phenix is GPL-3.0. [KNOWN]
- **Mac fit:** `x86-only`. Both sit on minimega. phenix ships an amd64 .deb and recommends Ubuntu 24.04. [KNOWN]
- **You learn:** "Emulytics," Sandia's word for running a cyber experiment many times and measuring the results. [KNOWN]
- **Sources:** [FIREWHEEL](https://github.com/sandialabs/firewheel), [phenix](https://github.com/sandialabs/sceptre-phenix), [Emulytics page](https://www.sandia.gov/emulytics/), [DOE CODE record](https://www.osti.gov/doecode/biblio/163934)

### CTADL (gem)

- **What:** static taint analysis. It traces how data flows from a "source" (like user input) to a "sink" (like a command). Works on Java/Android and on Ghidra P-code. [KNOWN]
- **Alive:** v0.14.0 in 2026-04. A new Rust version (ctadl-rs) is under active work. [KNOWN]
- **License:** not detected by GitHub. [UNKNOWN] Check the repo's license file before reuse.
- **Mac fit:** `arm-ok`. The README says it runs on macOS. You must build the Souffle engine first. [KNOWN]
- **You learn:** how code scanners find injection bugs. This is the theory behind SAST tools.
- **Try this:** use its hand-written "taint-front" examples first, before real apps. [INFERRED]
- **Sources:** [repo](https://github.com/sandialabs/ctadl), [docs](https://ctadl.readthedocs.io/en/latest/)

### packet2vec (gem)

- **What:** turns packet captures into word-style embeddings (Word2Vec) for machine learning. [KNOWN]
- **Alive:** no. Last commit 2022-07. [KNOWN]
- **License:** BSD 2-Clause. [KNOWN]
- **Mac fit:** `arm-partial`. Needs CMake and Boost to compile. Likely builds on ARM, not tested. [INFERRED]
- **You learn:** how ML people turn packets into numbers.
- **Sources:** [repo](https://github.com/sandialabs/packet2vec)

### Parseus

- **What:** a web app for Modbus data: read device registers, check function codes, train "known-good" models and spot oddities. [KNOWN]
- **Alive:** v1.0.0 on 2026-10-31. [KNOWN]
- **License:** GPL-3.0. [KNOWN]
- **Mac fit:** `x86-only`. README says Linux x86_64 only. [KNOWN]
- **Sources:** [repo](https://github.com/sandialabs/parseus)

### Also from Sandia

- **MasQiTT:** reference code for a Secure MQTT protocol using identity-based crypto. C. Last commit 2025-04. Apache 2.0. [KNOWN] [repo](https://github.com/sandialabs/MasQiTT)
- **mac-sandbox:** a macOS malware sandbox built on Cuckoo. Dead since 2016. History only. [KNOWN] [repo](https://github.com/sandialabs/mac-sandbox)

---

## Lawrence Berkeley National Laboratory (LBNL)

Orgs: `BerkeleyLab` (mostly accelerator code), `lbnl-cybersecurity` (20 repos), and ESnet (`esnet`), the DOE science network LBNL runs. [KNOWN]

### Zeek (born here)

- **What:** the network security monitor behind your Lab 5. It started at LBNL as "Bro." [KNOWN]
- **Alive:** very. v9.0.1 on 2026-10-26. Now run by its own open project. [KNOWN]
- **Mac fit:** `arm-ok`. Homebrew has Apple Silicon builds. [KNOWN]
- **Why it is here:** it is the single most useful thing any lab on this list ever released. [INFERRED]
- **Sources:** [repo](https://github.com/zeek/zeek), [LBNL cyber R&D page](https://secpriv.lbl.gov/), [OSTI record for Bro](https://www.osti.gov/biblio/1245188)

### Physics-based intrusion detection (gem)

- **What:** Bro scripts that watch traffic to a physical system and check it against physics. Example: "this command would make the tank overflow." Comes with simulations and traces. [KNOWN]
- **Alive:** no. Last commit 2014. Uses old Bro syntax. [KNOWN]
- **License:** not detected by GitHub. [UNKNOWN]
- **Mac fit:** `arm-partial`. The ideas port to modern Zeek. The old Broccoli library likely will not build. [INFERRED]
- **You learn:** a smart idea from the ICS world: detect attacks by their physical effect, not just their packets.
- **Try this:** read the scripts as a design study. Then sketch the same check as a modern Zeek script on Modbus logs from ICSNPP. [INFERRED]
- **Sources:** [repo](https://github.com/lbnl-cybersecurity/LBNL_Physics_Based_IDS), [DOE CODE record](https://www.osti.gov/doecode/biblio/6464)

### ESnet Holiday Hack write-up (gem)

- **What:** ESnet's security team's full write-up of the SANS Holiday Hack 2018 challenge, plus the tools they wrote. [KNOWN]
- **Alive:** a finished report from 2019. [KNOWN]
- **License:** BSD 3-Clause. [KNOWN]
- **Mac fit:** `web`. Read it in a browser. [KNOWN]
- **You learn:** how a real defense team thinks through recon, DNS, certificate logs and more.
- **Sources:** [write-up](https://software.es.net/sans-holiday-hack-2018/), [repo](https://github.com/esnet/sans-holiday-hack-2018)

### Also from LBNL and ESnet

- **cookiecutter-zeekpackage:** a template for starting your own Zeek package. Useful once you write Zeek scripts. [KNOWN] [repo](https://github.com/esnet/cookiecutter-zeekpackage)
- **SPARCS:** reads grid sensor (micro-PMU) data for real-time security. Old (2018), CentOS install. [KNOWN] [repo](https://github.com/lbnl-cybersecurity/sparcs)

---

## Pacific Northwest National Laboratory (PNNL)

GitHub org: `pnnl` (about 560 repos). Cyber work leans on machine learning. [KNOWN]

### safekit

- **What:** deep learning for insider threat and anomaly detection on log streams. Built around research papers that used LANL's datasets. [KNOWN]
- **Alive:** no. Last commit 2020-11. TensorFlow 1 era. [KNOWN]
- **License:** MIT. [KNOWN]
- **Mac fit:** `arm-partial`. Old TensorFlow 1 will be painful on Apple Silicon. Read it, do not fight it. [INFERRED]
- **You learn:** how "user behavior analytics" works under the hood.
- **Sources:** [repo](https://github.com/pnnl/safekit), [DOE CODE record](https://www.osti.gov/doecode/biblio/7199)

### V2W-BERT

- **What:** maps software vulnerabilities (CVEs) to weakness types (CWEs) with a language model. [KNOWN]
- **Alive:** no. Last commit 2022-02. [KNOWN]
- **License:** not detected by GitHub. [UNKNOWN]
- **Mac fit:** `arm-partial`. PyTorch runs on Apple Silicon. Python 3.7 pins may need updating. [INFERRED]
- **You learn:** the CVE vs CWE difference, which is a Security+ topic. [INFERRED]
- **Heads up:** the prepared dataset is a Google Drive link. The repo also has a script to build it from NVD yourself. [KNOWN]
- **Sources:** [repo](https://github.com/Cybersecurity-Tools/V2W-BERT)

### Agent Cage

- **What:** a Docker sandbox that gives an AI agent a full Ubuntu box, while the operator controls its network with a proxy, TLS inspection, allow lists and audit logs. [KNOWN]
- **Alive:** v0.1.0 in 2026-06. Marked a research prototype. [KNOWN]
- **License:** not detected by GitHub. [UNKNOWN]
- **Mac fit:** `arm-ok`. Docker plus Python. The README has macOS install notes. [KNOWN]
- **You learn:** egress control and TLS inspection, the same tools companies use on employees.
- **Sources:** [repo](https://github.com/pnnl/agent-cage)

### Also from PNNL

- **pcapgen:** Go code that generates PCAP puzzle files. Tiny and early. [KNOWN] [repo](https://github.com/pnnl/pcapgen)
- **FLOWER:** a network flow analyzer. Dormant since 2022. [KNOWN] [repo](https://github.com/pnnl/FLOWER)

---

## Los Alamos National Laboratory (LANL)

GitHub org: `lanl` (about 680 repos), almost all science and HPC. Very little cyber code. [KNOWN]

### LANL cyber security datasets

- **What:** three de-identified datasets from LANL's own network. [KNOWN]
  - **Comprehensive, Multi-Source:** 58 days. Logins, process starts, DNS, network flows, and marked red team events. About 1.6 billion events. [KNOWN]
  - **Unified Host and Network:** about 90 days of Windows host logs plus router flows. [KNOWN]
  - **User-Computer Authentication:** 9 months, about 708 million logins. [KNOWN]
- **Alive:** static datasets. Still online. [KNOWN]
- **Mac fit:** `arm-ok`. Plain compressed text. But they are huge. Use one day or one file. [INFERRED]
- **You learn:** real-scale log analysis. Can you find the red team logins in a sea of normal ones?
- **Try this:** take one daily auth file. Count logins per user. Look for a user who suddenly logs into many new computers. Pairs with Lab 4. [INFERRED]
- **Sign-up wall:** the download pages ask for your email and how you will use the data. The landing pages are public. Decide whether you are fine sharing an email first. [KNOWN]
- **Sources:** [dataset index](https://csr.lanl.gov/data/), [multi-source](https://csr.lanl.gov/data/cyber1/), [unified host and network](https://csr.lanl.gov/data/2017/), [authentication](https://csr.lanl.gov/data/auth/)

### Also from LANL

- **rhelhostinfo:** lists security-relevant facts about a RHEL host. Archived. [KNOWN] [repo](https://github.com/lanl/rhelhostinfo)

---

## Argonne National Laboratory

Orgs: `Argonne-National-Laboratory` (43 repos), `ANL-CEEESA` (grid and energy). [KNOWN]

### Cyber Defense Competition code (gem)

- **What:** code from DOE's 2016 cyber defense competition. Includes a mock industrial plant: an HMI, Modbus "electrical mains," and an emergency shutdown script. [KNOWN]
- **Alive:** no. Last commit 2018. Python 3.5 era. [KNOWN]
- **License:** not detected by GitHub. [UNKNOWN]
- **Mac fit:** `arm-partial`. Python runs, but old dependencies may break. [INFERRED]
- **You learn:** what a tiny fake ICS looks like inside. Point Zeek with ICSNPP at it, in your isolated lab only. [INFERRED]
- **Sources:** [repo](https://github.com/Argonne-National-Laboratory/cyber-defense-competition)

### CyberForce Program

- **What:** DOE's workforce program run by Argonne. Red vs blue team competitions on cyber-physical scenarios, monthly public webinars, and a "101 Library" of terms. [KNOWN]
- **Who:** the main competition is for college students. [KNOWN] Whether any part is open to high school students is [UNKNOWN].
- **Mac fit:** `web`.
- **Sources:** [CyberForce site](https://cyberforce.energy.gov/), [Argonne program page](https://www.anl.gov/sss/cyberforcer-program)

### Skipped on purpose

- **AdCyDER Attack Simulator** (ANL-CEEESA): it runs attacks on ICS and needs Metasploit. That is attack tooling, so it stays out of this repo. [KNOWN]

---

## NREL (now the National Laboratory of the Rockies, NLR)

GitHub org moved to `NatLabRockies` (about 820 repos). The old `NREL` org shows 0 repos. [KNOWN]

- **What it does publish:** grid and energy science. Cyber is rare. [KNOWN]
- **DSS-SimPy-RL:** a reinforcement learning playground for a cyber-physical power grid. Archived, last commit 2023-05. MIT. `arm-partial` (conda env). [KNOWN] [repo](https://github.com/NatLabRockies/DSS-SimPy-RL)
- **ModuleOT:** an OT module in C. Archived, last commit 2021-12. BSD 3-Clause. [KNOWN] [repo](https://github.com/NatLabRockies/ModuleOT)
- **Listed but not posted:** DOE CODE lists NREL cyber tools like HIDES (hybrid intrusion detection) and IViz-OT (an OT intrusion visualizer). I found no public repo for either. [INFERRED] [HIDES record](https://www.osti.gov/doecode/biblio/78045), [IViz-OT record](https://www.osti.gov/doecode/biblio/78539)
- **Lab page:** [NLR cybersecurity research](https://www.nlr.gov/security-resilience/cybersecurity)

---

## Brookhaven National Laboratory (BNL)

- **Found:** nothing learnable. The `bnl` GitHub org has 6 repos, all physics and X-ray science. `BNLNPPS` is nuclear physics software. [KNOWN]
- **Lab page:** BNL's cyber page is its internal IT security office, not research. [KNOWN] [page](https://www.bnl.gov/cybersecurity/)

---

## Which labs publish little or nothing

- **Brookhaven:** nothing found. [KNOWN]
- **NREL/NLR:** registers cyber software in DOE CODE but rarely posts the code. [INFERRED]
- **LANL:** almost no cyber code. Its datasets are the real contribution. [KNOWN]
- **Argonne:** the competition program, not tools. [INFERRED]
- **LBNL:** Zeek is huge, but its own cyber org is small and mostly pre-2020. [KNOWN]

## Where I searched

- GitHub orgs, every public repo listed and filtered by keyword: `idaholab`, `IdahoLabResearch`, `IdahoLabUnsupported`, `cisagov` (INL-built repos only), `sandialabs`, `sandia-minimega`, `llnl`, `pnnl`, `lanl`, `Argonne-National-Laboratory`, `ANL-CEEESA`, `NatLabRockies`, `NREL`, `BerkeleyLab`, `lbnl-cybersecurity`, `esnet`, `bnl`, `BNLNPPS`.
- OSTI API, software records, searched for: cyber, cybersecurity, intrusion detection, malware, network security, industrial control, reverse engineering, Zeek, SBOM, honeypot, threat. About 250 lab records came back.
- DOE CODE record pages for the tools cited above.
- Official lab pages: Sandia Emulytics and minimega, LBNL secpriv, PNNL cybersecurity, NLR cybersecurity, Argonne CyberForce, LANL csr.lanl.gov, LLNL CSI, BNL cybersecurity.

## Limits of this search

- DOE CODE's own search page needs JavaScript, so I used the OSTI API instead. A tool could be in DOE CODE but missed by my keywords. [INFERRED]
- inl.gov and anl.gov block plain page fetches. I relied on their GitHub repos and DOE CODE records instead. [KNOWN]
- I did not run any of these tools for this note. Mac fit comes from docs, release files and Homebrew. Treat `arm-ok` as "should work," then prove it in a lab. [KNOWN]
- Nothing opened here was marked CUI, OUO or export controlled. [KNOWN]
