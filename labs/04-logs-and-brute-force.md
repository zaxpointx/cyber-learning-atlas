# Lab 4: Read login logs and catch a brute-force attack

**Goal:** see what password guessing looks like in logs, then block it automatically.
**Time:** 1 to 2 hours. **Level:** beginner.
**ATT&CK:** [T1110 Brute Force](https://attack.mitre.org/techniques/T1110/), [T1078 Valid Accounts](https://attack.mitre.org/techniques/T1078/), [T1133 External Remote Services](https://attack.mitre.org/techniques/T1133/).
**D3FEND:** [Authentication Event Thresholding](https://d3fend.mitre.org/technique/d3f:AuthenticationEventThresholding/).
**Covers:** Security+ indicators of malicious activity, log analysis.

## Setup

`target` VM with SSH password login **temporarily turned on** (undo Lab 3's change for this lab only), and a throwaway user `labuser` with a weak password. Clone the VM first.

## Steps

1. **Watch the log live** on `target`: `sudo journalctl -u ssh -f`
2. **Fail on purpose** from `parrot`: try `ssh labuser@<target-ip>` with wrong passwords 10 times. Watch each "Failed password" line appear.
3. **Automate it like an attacker would,** with a tiny wordlist you write yourself (5 to 10 words, include the real one): `hydra -l labuser -P mywords.txt -t 2 ssh://<target-ip>`. Only against your own `target` VM.
4. **Count it:** `sudo journalctl -u ssh --since "10 min ago" | grep -c "Failed password"`
5. **Spot the success after the failures.** Find the "Accepted password" line. That pattern (many failures, then one success) is the alert defenders care about most.
6. **Block it automatically:** install CrowdSec (`sudo apt install crowdsec`) or fail2ban on `target`, rerun step 3, and confirm `parrot` gets blocked (`sudo cscli decisions list` for CrowdSec).
7. **Clean up:** delete `labuser`, turn password login back off.

## Check yourself

- Why is "failures then a success from the same IP" scarier than failures alone?
- How would MFA have changed this attack? (Hint: [Colonial Pipeline](../incidents/colonial-pipeline-2021.md) and [Change Healthcare](../incidents/change-healthcare-2024.md).)

## Write-up

Paste the key log lines, your detection idea in plain words, and how CrowdSec or fail2ban decided to block.
