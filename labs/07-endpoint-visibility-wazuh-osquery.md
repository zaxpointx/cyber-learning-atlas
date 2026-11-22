# Lab 7: Endpoint visibility with Wazuh and osquery

**Goal:** run a free SIEM, connect your target VM, and catch persistence tricks like new users and changed system files.
**Time:** 3 to 4 hours. **Level:** intermediate.
**ATT&CK:** [T1136](https://attack.mitre.org/techniques/T1136/), [T1098](https://attack.mitre.org/techniques/T1098/), [T1547](https://attack.mitre.org/techniques/T1547/), [T1059](https://attack.mitre.org/techniques/T1059/), [T1685](https://attack.mitre.org/techniques/T1685/).
**D3FEND:** [System File Analysis](https://d3fend.mitre.org/technique/d3f:SystemFileAnalysis/), [User Account Permissions](https://d3fend.mitre.org/technique/d3f:UserAccountPermissions/), [Operational Process Monitoring](https://d3fend.mitre.org/technique/d3f:OperationalProcessMonitoring/).
**Covers:** Security+ security operations (SIEM, endpoint monitoring).

## Setup

- `sensor` VM with at least 6 to 8 GB RAM. Wazuh's central components support 64-bit Intel, AMD or ARM Linux. [KNOWN: Wazuh docs] The `wazuh/wazuh-manager` Docker image has arm64 builds. [KNOWN: Docker Hub]
- Follow Wazuh's official install guide (the single-node Docker deployment is the easiest): https://documentation.wazuh.com/current/index.html
- Install the Wazuh agent on `target` and point it at the sensor.
- Install osquery on `target` from https://osquery.io/ (official Linux aarch64 packages exist). [KNOWN: osquery GitHub releases]

## Steps

1. **Baseline:** in the Wazuh dashboard, look at the alerts from `target` for 10 minutes of normal use. That's "normal".
2. **Create a user** on `target`: `sudo useradd -m backdoor_test`. Find the alert in Wazuh.
3. **Change a watched file:** Wazuh's file integrity monitoring watches `/etc` by default on Linux. [INFERRED: check `ossec.conf` syscheck section] Edit `/etc/hosts` and find the alert.
4. **Add an SSH key** to a user's `~/.ssh/authorized_keys` and see if Wazuh notices. If not, add that path to syscheck and try again.
5. **Ask osquery questions:**
   ```sql
   SELECT username, uid, shell FROM users WHERE shell NOT LIKE '%nologin%';
   SELECT * FROM crontab;
   SELECT name, path, cmdline FROM processes WHERE on_disk = 0;
   SELECT * FROM listening_ports;
   ```
   (Run `osqueryi` to get the prompt.)
6. **Simulate a defender being blinded:** stop the agent (`sudo systemctl stop wazuh-agent`) and see how the dashboard shows the agent as disconnected. That's what [T1685](https://attack.mitre.org/techniques/T1685/) looks like from the SOC.
7. **Clean up:** delete `backdoor_test`, undo file changes, restart the agent.

## Check yourself

- Which of your actions generated the loudest alert? The quietest?
- Why does Volt Typhoon's "living off the land" make baselines so important? ([incident](../incidents/volt-typhoon-2024.md))

## Write-up

A table of each action, whether Wazuh caught it, and the rule ID that fired.
