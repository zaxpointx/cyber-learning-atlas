# Lab 2: Harden your Cisco 1941 router

**Goal:** lock down your router the way real network defenders do, using the same checklist that came out of the Salt Typhoon advisory.
**Time:** 2 to 3 hours. **Level:** beginner to intermediate.
**ATT&CK:** [T1190](https://attack.mitre.org/techniques/T1190/), [T1136](https://attack.mitre.org/techniques/T1136/), [T1098](https://attack.mitre.org/techniques/T1098/), [T1572](https://attack.mitre.org/techniques/T1572/).
**D3FEND:** Application Configuration Hardening, Change Default Password, Credential Hardening, Network Isolation (all listed in CISA AA25-239A's mitigation table). [KNOWN]
**Covers:** Network+ network security, Security+ hardening.

## First, the honest part about your router

Cisco's end-of-life notice for the Cisco ONE 1941 and 1921 bundles lists the end of vulnerability and security support as **September 28, 2021** and the last date of support as **September 30, 2023**. [KNOWN: Cisco EOL notice EOL12141, https://www.cisco.com/c/en/us/products/collateral/routers/1900-series-integrated-services-routers-isr/eos-eol-notice-c51-740520.html] The plain CISCO1941/K9 part has its own notice, which we haven't confirmed, but it is from the same era. [INFERRED]

**What this means for you:** no new security fixes. It's a great lab router and a bad internet router. Keep it inside your lab.

## Setup

- Console cable from the Mac mini to the router (the 1941 has an RJ-45 console port and a USB console port). Connect with `screen /dev/tty.usbserial-XXXX 9600` (find the name with `ls /dev/tty.*`).
- Optional: a cable from the router's `GigabitEthernet0/0` to a lab VM via a UTM bridged interface, so you can test SSH and syslog.
- Save the current config first: `show running-config` and copy it into `lab-notes.md`. That's your "before" picture.

## Steps

1. **Record your software version:** `show version`. Look the version up in the [Cisco Software Checker](https://sec.cloudapps.cisco.com/security/center/softwarechecker.x) and note which advisories apply.
2. **Look for problems first** (this is how you'd check a router you suspect is hacked):
   ```
   show running-config | include username|snmp|http|access-list|tunnel|transport
   show users
   show ip interface brief
   ```
   AA25-239A says attackers often added ACLs, turned on SSH on odd high ports, enabled HTTP servers and abused SNMP with default community strings like "public" and "private". [KNOWN]
3. **Turn off the web server:**
   ```
   conf t
   no ip http server
   no ip http secure-server
   ```
4. **Strong secrets and a local admin user:**
   ```
   enable algorithm-type scrypt secret <long-passphrase>
   username admin privilege 15 algorithm-type scrypt secret <different-long-passphrase>
   ```
   If your IOS doesn't support `algorithm-type`, use `enable secret` (never `enable password`). [INFERRED: depends on IOS version; check with `enable ?`]
5. **SSH only, from your lab only:**
   ```
   ip domain-name lab.local
   crypto key generate rsa modulus 2048
   ip ssh version 2
   ip access-list standard MGMT
    permit 192.168.64.0 0.0.0.255
   line vty 0 4
    transport input ssh
    login local
    access-class MGMT in
    exec-timeout 10 0
   ```
6. **Slow down password guessing:** `login block-for 120 attempts 3 within 60`
7. **Kill SNMP v1/v2c:** remove any `snmp-server community` lines (`no snmp-server community public` and so on). If you want SNMP, learn SNMPv3 with authentication and privacy, as the advisory recommends. [KNOWN: AA25-239A]
8. **Log everything to your sensor VM:**
   ```
   service timestamps log datetime msec
   logging host <sensor-ip>
   logging trap informational
   archive
    log config
     logging enable
     notify syslog
   ```
   The `archive log config` part logs every config change, so you'd see an attacker adding a user.
9. **Turn off things you don't use:** `no ip source-route`, `no service pad`, `no ip bootp server`, and `no cdp run` if you don't need CDP.
10. **Save and diff:** `copy running-config startup-config`, then copy the new `show running-config` into your notes and compare with the "before" copy.

## Check yourself

- From `parrot`, does `ssh admin@<router-ip>` work? Does `telnet <router-ip>` fail?
- From an IP outside the MGMT list, is SSH refused?
- Do failed logins show up in the router log and on your sensor?

## Write-up

Before/after table of every change, the CVEs the Software Checker found, and which line of AA25-239A's D3FEND table each change matches. Then read [Salt Typhoon](../incidents/salt-typhoon-2025.md) and explain in your own words how your changes would have helped.

## Sources

- CISA AA25-239A: https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a
- Cisco IOS hardening guide: https://sec.cloudapps.cisco.com/security/center/resources/IOS_hardening
- CISA communications infrastructure hardening guidance: https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure
