# Lab 0: Build a safe lab on your Mac

**Goal:** three VMs on a private network you control, with a clean way to roll back.
**Time:** 2 to 3 hours. **Level:** beginner.
**Covers:** Security+ Security Architecture (segmentation), Network+ basics.

## What you need

- Mac mini (Apple Silicon) with [UTM](https://mac.getutm.app/) installed.
- [Parrot OS](https://parrotsec.org/) ARM64. Parrot offers an ARM64 ISO and a ready-made UTM image for Apple Silicon. [KNOWN: Parrot download page]
- [Ubuntu Server for ARM](https://ubuntu.com/download/server/arm) for the target and sensor VMs.

## The lab layout

| VM | OS | Job | Suggested RAM |
|---|---|---|---|
| `parrot` | Parrot OS ARM64 | Your attacker and analyst box | 4 GB |
| `target` | Ubuntu Server ARM | The machine you attack and defend | 2 GB |
| `sensor` | Ubuntu Server ARM | Runs Zeek, Suricata, Wazuh later | 6 to 8 GB |

If your Mac mini has 16 GB of RAM or less, only run two VMs at a time. [INFERRED: Wazuh and the OS need room]

## Steps

1. **Install the VMs.** Create each VM in UTM with the "Virtualize" option (fast, ARM). Avoid "Emulate" (x86), which is much slower on Apple Silicon. [INFERRED from UTM's design]
2. **Install updates while online.** Leave the network on **Shared Network** at first, run `sudo apt update && sudo apt full-upgrade`, and install what later labs need: `sudo apt install -y openssh-server nmap tcpdump curl git docker.io`.
3. **Switch to an isolated network for attack labs.** In each VM's settings, set Network Mode to **Host Only**. UTM's docs say Host Only blocks internet (WAN) traffic so the guest can't reach the internet. [KNOWN: UTM network docs] Use **Shared Network** again only when you need to install something.
4. **Give each VM a fixed IP** on the host-only subnet if DHCP isn't provided (UTM docs note host networks may not provide DHCP). Write the IPs down in a `lab-notes.md`.
5. **Test the network.** From `parrot`, `ping` the other two VMs. Then confirm the internet is blocked: `curl -m 5 https://example.com` should fail while in Host Only mode.
6. **Make a rollback copy.** Shut each VM down and use UTM's Clone option to make a "clean" copy. Before any risky lab, clone again (or restore from the clean copy).
7. **Create a non-admin user** on each VM for daily use, and keep a strong password for the admin one.

## Check yourself

- Can you explain the difference between Shared Network and Host Only?
- If a VM got infected, how would you get back to clean in under 5 minutes?

## Write-up

Use [WRITEUP-TEMPLATE.md](WRITEUP-TEMPLATE.md). Include a simple diagram of your lab network with IPs.
