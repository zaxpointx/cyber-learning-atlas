# Real world layer: where this work happens at ORNL and Y-12

This page connects what you practice here to the public work of two Oak Ridge sites, using the separate research atlas at https://github.com/zaxpointx/ornl-public-tech-research. That atlas tags its own claims as Known, Inferred or Unknown with sources; open the linked page for evidence. Neither repo is affiliated with ORNL, Y-12, UT-Battelle, CNS, NNSA or DOE.

**Key takeaway:** ORNL's public cyber work is mostly *research* (inventing new defenses for vehicles, the grid and AI), while Y-12's is mostly *operations* (a 24/7 SOC protecting a high-security site). Labs 4 through 8 here build the SOC skills that both sides list; ORNL's research adds data science and embedded systems on top. [INFERRED from both atlases]

## Topic by topic

| Topic in this repo | Where it shows up at ORNL or Y-12 | Atlas page | Labs here |
|---|---|---|---|
| Network monitoring and IDS (Zeek, Suricata) | The Y-12 atlas's study list for the NOC/SOC track includes a SIEM, Snort or Suricata IDS and packet capture. ORNL's AI cyber engineer post names "file and network traffic analysis". | [Y-12 learn and build](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/y12/learn-and-build.md), [ORNL learn and build](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/learn-and-build.md) | [5](../labs/05-network-sensor-zeek-suricata.md), [6](../labs/06-detection-rules-sigma-yara.md) |
| SIEM and endpoint monitoring (Wazuh) | The Y-12 SOC post prefers Network+, Security+ and Splunk. A "home SOC in a box" is the atlas's top project idea for Y-12. | [Y-12 learn and build](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/y12/learn-and-build.md) | [7](../labs/07-endpoint-visibility-wazuh-osquery.md) |
| Linux persistence and forensic diffing | ORNL's Systemd Snapshot tool maps and diffs systemd boot dependencies; it's the easiest ORNL repo to run. | [ORNL cyber atlas](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/README.md) | [7](../labs/07-endpoint-visibility-wazuh-osquery.md), [8](../labs/08-adversary-emulation-atomic-red-team.md) |
| Detection on vehicle networks (CAN bus) | ORNL's most active public cyber lane: CANRate, the ROAD dataset (CC BY 4.0) and related detectors. | [Vehicle cyber deep dive](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/deep-dives/vehicle-cyber.md) | [6](../labs/06-detection-rules-sigma-yara.md) (detection thinking) |
| Grid and industrial security (ICS) | ORNL's grid security work (Cyber Grid Guard, CyTRICS) and the Ukraine 2015 attack it guards against. | [Grid and quantum security deep dive](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/deep-dives/grid-and-quantum-security.md) | [Ukraine incident](../incidents/ukraine-grid-2015.md), [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/) |
| AI and cyber defense | ORNL's Cyberwheel (MIT-licensed RL cyber defense simulator) and AI security center CAISER. | [AI security deep dive](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/deep-dives/ai-security.md) | [8](../labs/08-adversary-emulation-atomic-red-team.md) (attack simulation basics) |
| Analyst tools history | ORNL's open-source analyst tools from 2010 to 2019 (ORCA, Stucco, Situ, Akatosh) and why they went quiet. | [Analyst tools lineage](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/deep-dives/analyst-tools-lineage.md) | [5](../labs/05-network-sensor-zeek-suricata.md) |
| Small manufacturer security and file integrity | Y-12 and Los Alamos designed a cyber range copying small defense suppliers' networks; students built a tool to catch tampered machine files (G-code). | [Y-12 atlas](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/y12/README.md) | [6](../labs/06-detection-rules-sigma-yara.md) (YARA), [12](../labs/12-secrets-and-supply-chain.md) |
| Federal security controls (NIST) | Both sites operate under federal security rules; the ORNL and Y-12 atlases point to NIST SP 800-82 (OT) and SP 800-171 (suppliers). | [Y-12 learn and build](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/y12/learn-and-build.md) | [research/](../research/README.md) |
| Security clearances and career gates | Y-12 SOC jobs need a DOE Q clearance; its summer internships start at college junior standing. ORNL research jobs usually want a degree and clearance. | [Y-12 learn and build](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/y12/learn-and-build.md), [ORNL learn and build](https://github.com/zaxpointx/ornl-public-tech-research/blob/main/atlas/cyber/learn-and-build.md) | Your write-ups are the portfolio for when those doors open. |

## A project that bridges both repos

**Build a home SOC, then point it at ORNL-style data.** Do Labs 5 to 8, then use the public ROAD CAN dataset from the ORNL atlas's vehicle deep dive to write a simple timing-based detector, and document it the way this repo documents labs. That joins "SOC operations" (Y-12 style) with "detection research" (ORNL style) in one portfolio piece. [INFERRED: our suggestion]

## Rules carry over

Same rules as both repos: public info only, no claims of affiliation, no contacting lab staff through these projects, nothing export-controlled.
