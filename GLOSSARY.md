# Glossary

Plain-word definitions for terms used across the repo. Agents: add new terms in alphabetical order.

| Term | Plain meaning |
|---|---|
| **ACL (access control list)** | A list of rules on a router or firewall that says which traffic is allowed and which is blocked. |
| **Adversary emulation** | Safely copying what real attackers do, in your own lab, to see if your defenses notice. |
| **APT (advanced persistent threat)** | A skilled, well-funded attacker group (often tied to a government) that stays hidden in a network for a long time. |
| **ATT&CK** | MITRE's public catalog of how real attackers operate, organized by goal (tactic) and method (technique). |
| **Blue team** | Defenders. Red team is attackers (in a test). Purple team is both working together. |
| **C2 (command and control)** | How an attacker sends orders to a hacked machine and gets data back. |
| **CTF (capture the flag)** | A hacking competition or practice puzzle where you find a hidden "flag" string to prove you solved it. |
| **CVE** | A public ID number for a specific known vulnerability, like CVE-2021-44228 (Log4Shell). |
| **D3FEND** | MITRE's catalog of defensive techniques, the counterpart to ATT&CK. |
| **Detection engineering** | Writing and testing the rules that make alerts fire when something bad happens. |
| **EDR (endpoint detection and response)** | Security software on a computer that watches what programs do and can stop bad behavior. |
| **EICAR test file** | A harmless text string every antivirus treats as "malware" on purpose, so you can test detection safely. |
| **Edge device** | Anything sitting at the border between your network and the internet: routers, firewalls, VPN boxes. Attackers love these. |
| **Exfiltration** | Stealing data out of a network. |
| **IDS / IPS** | Intrusion detection system (watches and alerts) / intrusion prevention system (watches and blocks). Suricata can do both. |
| **IOC (indicator of compromise)** | A clue left behind by an attack, like a bad IP address or file hash. |
| **KEV** | CISA's Known Exploited Vulnerabilities catalog: CVEs that attackers are actually using. Patch these first. |
| **Lateral movement** | Moving from the first hacked computer to others in the same network. |
| **Living off the land** | Attacking with tools already built into the system (PowerShell, SSH, cron) so nothing new looks suspicious. |
| **MFA (multi-factor authentication)** | Needing a second proof (app code, security key) besides a password. Phishing-resistant MFA (security keys, passkeys) is the strongest kind. |
| **NIDS / HIDS** | Network-based vs host-based intrusion detection. Zeek and Suricata are network; Wazuh and osquery are host. |
| **Pcap** | A saved file of captured network traffic, opened with Wireshark or Zeek. |
| **Persistence** | How an attacker makes sure they stay in after a reboot or password change. |
| **Ransomware** | Malware that locks (encrypts) files and demands payment. Most groups now also steal data first and threaten to leak it. |
| **SIEM** | A system that collects logs from many machines in one place so you can search them and alert on patterns. Wazuh includes one. |
| **Sigma** | A shared format for writing detection rules for logs, which can be converted for many SIEMs. |
| **SNMP** | A protocol for managing network gear. Old versions (v1/v2c) use plain-text "community strings" like "public"; use v3. |
| **SOC (security operations center)** | The team (and room) that watches alerts 24/7 and responds to incidents. |
| **Supply chain attack** | Breaking into a trusted vendor or software project so their update or package carries the attack to everyone else. |
| **Tactic / technique** | In ATT&CK, the tactic is the attacker's goal (like "Persistence") and the technique is how they do it (like "Scheduled Task/Job"). |
| **Tabletop exercise** | Talking through a pretend incident step by step to practice decisions, no computers needed. |
| **UTM** | The free virtual machine app for macOS used in this repo's labs. On Apple Silicon it runs ARM guests fast and emulates x86 slowly. |
| **VM (virtual machine)** | A computer running inside your computer. You can snapshot it and roll back if you break it. |
| **YARA** | A rule language for describing and finding files by patterns, used for malware research. |
| **Zero Trust** | Never trusting something just because it is inside the network. Every user and device has to prove itself every time. |
