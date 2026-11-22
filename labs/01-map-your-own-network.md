# Lab 1: Map your own network with Nmap and Wireshark

**Goal:** find every machine and open service in your lab, and see what a scan looks like on the wire.
**Time:** 1 to 2 hours. **Level:** beginner.
**ATT&CK:** [T1595 Active Scanning](https://attack.mitre.org/techniques/T1595/), [T1046 Network Service Discovery](https://attack.mitre.org/techniques/T1046/).
**Covers:** Network+ ports and protocols, Security+ vulnerability scanning concepts.

## Setup

Lab 0 done. All VMs on Host Only. Wireshark on `parrot` (preinstalled on Parrot Security). Lab subnet written down (example below uses `192.168.64.0/24`; use yours).

## Steps

1. **Start a capture.** On `parrot`, open Wireshark on the lab interface.
2. **Find live hosts:** `nmap -sn 192.168.64.0/24`
3. **Find open ports on the target:** `nmap -sT -p- <target-ip>`
4. **Find versions:** `nmap -sV -p 22 <target-ip>`
5. **Stop the capture** and filter with `tcp.flags.syn == 1 && tcp.flags.ack == 0`. That's every connection attempt the scan made.
6. **Compare with a "quiet" scan:** run `sudo nmap -sS --top-ports 100 <target-ip>` and see how the packets differ from `-sT`.
7. **Look at it from the target's side:** on `target`, run `sudo tcpdump -n -i any not port 22` while you scan again.

## Check yourself

- What's the difference between `-sT` and `-sS`?
- Why does `-sV` create more traffic?
- Which Wireshark filter shows only traffic from the scanner?

## Write-up

List every host and open port you found (an "asset inventory"), and paste one screenshot of the scan in Wireshark. Asset inventory is the first thing defenders need. [KNOWN: CIS Controls 1 and 2 are asset and software inventory]

**Rule reminder:** only scan your lab subnet. Nmap's own docs discuss the legal risks of scanning networks you don't own: https://nmap.org/book/man-legal.html
