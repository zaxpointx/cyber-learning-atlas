# Lab 3: Harden a Linux VM with Lynis

**Goal:** audit your `target` VM, fix the top findings, and measure the improvement.
**Time:** 1 to 2 hours. **Level:** beginner.
**D3FEND:** [Platform Hardening](https://d3fend.mitre.org/technique/d3f:PlatformHardening/), [Strong Password Policy](https://d3fend.mitre.org/technique/d3f:StrongPasswordPolicy/).
**Covers:** Security+ hardening techniques.

## Setup

`target` VM, temporarily on Shared Network to install: `sudo apt install -y lynis` (or clone from https://github.com/CISOfy/lynis).

## Steps

1. Run the audit: `sudo lynis audit system`
2. Write down the **Hardening index** score at the end, and the list of **Warnings** and **Suggestions** (also saved in `/var/log/lynis-report.dat`).
3. Pick 3 to 5 fixes you understand. Good first ones:
   - SSH: in `/etc/ssh/sshd_config`, set `PermitRootLogin no` and `PasswordAuthentication no` (after setting up an SSH key from `parrot` with `ssh-copy-id`). Restart with `sudo systemctl restart ssh`.
   - Turn on automatic security updates: `sudo apt install unattended-upgrades`.
   - Turn on a firewall: `sudo ufw allow from <lab-subnet> to any port 22 && sudo ufw enable`.
4. Run Lynis again and compare the score.

## Check yourself

- Why is disabling SSH password logins stronger than a long password?
- What could break if you turn on the firewall before allowing SSH?

## Write-up

Before and after scores, each fix, and why it matters, in one table.
