# Hands-on lab path

Twelve labs plus setup, Security+ level and up, all on your own Mac mini in UTM VMs (and your Cisco 1941). One lab a week gets you through in about three months.

**Read [SAFETY.md](SAFETY.md) first.** Every lab runs only on machines you own, on an isolated lab network.

After each lab, write it up with [WRITEUP-TEMPLATE.md](WRITEUP-TEMPLATE.md). The write-ups are your portfolio.

## The path

| # | Lab | Level | Time | Main tools | ATT&CK focus |
|---|---|---|---|---|---|
| 0 | [Build a safe lab](00-safe-lab-setup.md) | Beginner | 2 to 3 h | UTM, Parrot, Ubuntu | n/a |
| 1 | [Map your own network](01-map-your-own-network.md) | Beginner | 1 to 2 h | Nmap, Wireshark | T1595, T1046 |
| 2 | [Harden your Cisco router](02-harden-your-cisco-router.md) | Beginner+ | 2 to 3 h | IOS CLI | T1190, T1136, T1098, T1572 |
| 3 | [Harden a Linux VM](03-linux-hardening-lynis.md) | Beginner | 1 to 2 h | Lynis, ufw | Hardening |
| 4 | [Logs and brute force](04-logs-and-brute-force.md) | Beginner | 1 to 2 h | journalctl, Hydra, CrowdSec | T1110, T1078, T1133 |
| 5 | [Network sensor](05-network-sensor-zeek-suricata.md) | Intermediate | 3 to 4 h | Zeek, Suricata | T1046, T1071, T1021 |
| 6 | [Detection rules](06-detection-rules-sigma-yara.md) | Intermediate | 2 h | Sigma, YARA | T1110, T1105 |
| 7 | [Endpoint visibility](07-endpoint-visibility-wazuh-osquery.md) | Intermediate | 3 to 4 h | Wazuh, osquery | T1136, T1098, T1547, T1685 |
| 8 | [Adversary emulation](08-adversary-emulation-atomic-red-team.md) | Intermediate | 2 to 3 h | Atomic Red Team | T1053, T1136 |
| 9 | [Web app testing](09-web-app-testing-juice-shop.md) | Beginner+ | 2 to 4 h | Juice Shop, ZAP | T1190 |
| 10 | [Patch priorities with KEV](10-kev-patch-priorities.md) | Beginner | 1 to 2 h | kev_lookup.py, EPSS | T1190 |
| 11 | [Tabletop a real incident](11-tabletop-from-a-real-incident.md) | Beginner | 1 to 2 h | NIST 800-61r3, your agent | varies |
| 12 | [Secrets and supply chain](12-secrets-and-supply-chain.md) | Beginner | 1 to 2 h | Gitleaks, pre-commit | T1195, T1552 |

Times are our estimates. [INFERRED]

## Suggested order

0, 1, 2, 3, 4 (foundations) then 10, 12 (quick wins) then 5, 6, 7, 8 (the home SOC) then 9 and 11 whenever you want a change of pace.

**Key takeaway:** labs 5 through 8 together are a working home SOC: a network sensor, a SIEM, detection rules, and a way to test them. That's the same skill set the SOC job posts in the ORNL and Y-12 atlases ask for. See [real-world/](../real-world/README.md).

## Security+ V8 (SY0-801) domain map

CompTIA's new Security+ V8 launched November 17, 2026, with five domains. [KNOWN: CompTIA V8 page, https://www.comptia.org/en-us/certifications/security/v8/]

| Domain (exam weight) | Labs that practice it |
|---|---|
| General Security Concepts (16%) | 0, 3, 12 |
| Threats, Vulnerabilities, and Attacks (24%) | 1, 4, 9, 10 |
| Security Architecture (19%) | 0, 2, 3 |
| Security Operations (27%) | 4, 5, 6, 7, 8, 10, 11 |
| Security Program Management and Oversight (14%) | 10, 11 |

The mapping is ours. [INFERRED]

## My progress

Copy this into your own notes and check them off:

- [ ] Lab 0
- [ ] Lab 1
- [ ] Lab 2
- [ ] Lab 3
- [ ] Lab 4
- [ ] Lab 5
- [ ] Lab 6
- [ ] Lab 7
- [ ] Lab 8
- [ ] Lab 9
- [ ] Lab 10
- [ ] Lab 11
- [ ] Lab 12
