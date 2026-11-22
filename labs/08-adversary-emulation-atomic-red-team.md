# Lab 8: Test your defenses with Atomic Red Team

**Goal:** run small, safe tests that mimic real attacker techniques, and check whether Lab 7's Wazuh setup catches them.
**Time:** 2 to 3 hours. **Level:** intermediate.
**ATT&CK:** [T1053 Scheduled Task/Job](https://attack.mitre.org/techniques/T1053/), [T1059](https://attack.mitre.org/techniques/T1059/), [T1136](https://attack.mitre.org/techniques/T1136/), [T1003](https://attack.mitre.org/techniques/T1003/) (read only).
**Covers:** Security+ security operations, testing controls.

## Safety first

- Run only on the `target` VM, on Host Only networking, after cloning it.
- Read every test's YAML before you run it. Atomic tests change the system on purpose.
- Always run the cleanup command after each test.

## Setup

- Atomic Red Team test library: https://github.com/redcanaryco/atomic-red-team (MIT). Tests are organized as `atomics/T####/T####.yaml`. [KNOWN]
- Runner: Invoke-AtomicRedTeam, a PowerShell module that also works with PowerShell 7 on Linux. https://github.com/redcanaryco/invoke-atomicredteam [KNOWN]. Install PowerShell 7 for Linux ARM64 using Microsoft's official instructions.
- **No PowerShell?** You can read a test's YAML and type its commands by hand. Same learning, more manual.

## Steps

1. **Pick a technique:** start with T1053.003 (cron). Open `atomics/T1053.003/T1053.003.yaml` and read what each test does.
2. **Show details without running:** `Invoke-AtomicTest T1053.003 -ShowDetailsBrief`
3. **Check prerequisites:** `Invoke-AtomicTest T1053.003 -TestNumbers 1 -CheckPrereqs`
4. **Run one test:** `Invoke-AtomicTest T1053.003 -TestNumbers 1`
5. **Hunt for it** in Wazuh and with osquery (`SELECT * FROM crontab;`).
6. **Clean up:** `Invoke-AtomicTest T1053.003 -TestNumbers 1 -Cleanup`
7. **Repeat** with a Linux test for T1136.001 (create local account). For T1003, only read the tests and discuss with your agent how defenders detect them. Don't run credential dumping tests unless you fully understand them.
8. **Score yourself:** a simple table of technique, test, detected (yes/no), and how.

## Check yourself

- Which tests did your setup miss? What log source would you need to catch them?
- How is this different from just reading about ATT&CK?

## Write-up

Your detection scorecard plus one new Wazuh rule or Sigma rule that closes a gap you found. This is what "purple teaming" means.
