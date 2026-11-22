# Lab 10: Build a patch plan with KEV

**Goal:** inventory the software in your lab, check it against real-world exploitation data, and decide what to fix first.
**Time:** 1 to 2 hours. **Level:** beginner.
**ATT&CK:** [T1190](https://attack.mitre.org/techniques/T1190/).
**D3FEND:** [Software Inventory](https://d3fend.mitre.org/technique/d3f:SoftwareInventory/), [Software Update](https://d3fend.mitre.org/technique/d3f:SoftwareUpdate/).
**Covers:** Security+ vulnerability management.

## Setup

This repo cloned on `parrot` (or your Mac). Read [techniques/kev.md](../techniques/kev.md) first.

## Steps

1. **Inventory:**
   - Linux VMs: `dpkg -l | wc -l` then pick 10 important packages (`openssh-server`, `openssl`, `sudo`, `xz-utils`, `docker.io`...) with versions: `dpkg -l openssh-server openssl sudo xz-utils`
   - Router: `show version` from Lab 2.
2. **Check KEV:**
   ```bash
   python3 scripts/kev_lookup.py --vendor cisco --product ios
   python3 scripts/kev_lookup.py --vendor openssh
   python3 scripts/kev_lookup.py --ransomware --since 2026-01-01
   ```
3. **Check whether your exact version is affected.** KEV says a bug is exploited; it doesn't say *your* version is vulnerable. Use the vendor advisory (for Cisco, the [Software Checker](https://sec.cloudapps.cisco.com/security/center/softwarechecker.x)) or the CVE page on [NVD](https://nvd.nist.gov/).
4. **Add EPSS** for anything not on KEV: look it up at https://www.first.org/epss/
5. **Make the plan:** a table sorted by KEV first, then EPSS, then CVSS, with what you'll do (patch, disable the feature, replace, or accept the risk and why).
6. **Patch the VMs:** `sudo apt update && sudo apt full-upgrade` and re-check versions.

## Check yourself

- Why isn't "highest CVSS first" the best plan by itself?
- What do you do about the router if no patch will ever come? (Replace it or keep it isolated.)

## Write-up

Your patch plan table and a short paragraph on the router decision.
