# Lab 5: Build a network sensor with Zeek and Suricata

**Goal:** watch your lab network with the two tools real SOCs use, and catch your own scan.
**Time:** 3 to 4 hours. **Level:** intermediate.
**ATT&CK:** [T1046](https://attack.mitre.org/techniques/T1046/), [T1071](https://attack.mitre.org/techniques/T1071/), [T1021](https://attack.mitre.org/techniques/T1021/), [T1572](https://attack.mitre.org/techniques/T1572/).
**D3FEND:** [Network Traffic Analysis](https://d3fend.mitre.org/technique/d3f:NetworkTrafficAnalysis/), [Network Traffic Signature Analysis](https://d3fend.mitre.org/technique/d3f:NetworkTrafficSignatureAnalysis/).
**Covers:** Security+ security monitoring, Network+ traffic analysis.

## Setup

`sensor` VM on the same host-only network as `parrot` and `target`. Install while on Shared Network:

```bash
sudo apt install -y suricata docker.io
sudo docker pull zeek/zeek:latest     # official image, has arm64 builds
```

Suricata is in Ubuntu and Debian repos for arm64. Zeek isn't in Debian's repos, but the official Docker image supports arm64. [KNOWN: Debian package index, Docker Hub]

**Note:** the sensor can only see traffic that reaches it. The simplest way is to send traffic *to* the sensor or run the tools on `target` itself. Ask your agent about promiscuous mode if you want to see traffic between other VMs. [INFERRED]

## Steps

### Part A: Zeek

1. Capture 5 minutes of traffic: `sudo tcpdump -i <iface> -w lab.pcap` while you SSH from `parrot` and run `nmap -sT <sensor-ip>`.
2. Run Zeek on the pcap: `sudo docker run --rm -v $PWD:/pcap -w /pcap zeek/zeek zeek -r lab.pcap`
3. Read the logs: `conn.log`, `ssh.log`, `dns.log`. Try `cat conn.log | awk '{print $3}' | sort | uniq -c | sort -rn | head` to see which IP made the most connections.

### Part B: Suricata

1. Update rules: `sudo suricata-update` (downloads the free ET Open ruleset).
2. Add your own rule in `/etc/suricata/rules/local.rules`:
   ```
   alert tcp any any -> $HOME_NET 22 (msg:"LAB SSH connection attempt"; flags:S; sid:1000001; rev:1;)
   ```
   Add `local.rules` to `rule-files` in `/etc/suricata/suricata.yaml`, and set `HOME_NET` to your lab subnet.
3. Test the config: `sudo suricata -T -c /etc/suricata/suricata.yaml`
4. Run on the same pcap: `sudo suricata -r lab.pcap -l ./suri-out` and read `suri-out/fast.log` and `eve.json`.
5. Run it live: `sudo systemctl restart suricata` and `sudo tail -f /var/log/suricata/fast.log`, then scan again from `parrot`.

## Check yourself

- What does Zeek tell you that Suricata doesn't, and the other way around?
- What does your scan look like in `conn.log` (look at the `conn_state` column)?

## Write-up

One Zeek finding and one Suricata alert, explained. Include your custom rule and what each part means.

## Docs

- Zeek: https://docs.zeek.org/en/master/
- Suricata: https://docs.suricata.io/
