# Cisco IOS XE web UI mass exploitation (2023)

**Topic:** network-devices, vulnerability  
**Level:** beginner  
**Last checked:** 2026-11-22

## What happened

In October 2023 attackers exploited a bug in the web management interface of Cisco IOS XE routers and switches to create their own admin accounts and plant an implant on many devices. [KNOWN: Cisco Talos; Cisco advisory]

## How they got in and what went wrong

- CVE-2023-20198 let an attacker create an account with top privileges through the web UI, if the HTTP or HTTPS server feature was turned on and reachable. [KNOWN: Cisco advisory]
- A second bug, CVE-2023-20273, was used to run commands as root and install the implant. [KNOWN: Talos; also listed in CISA AA25-239A]
- Cisco's main advice was to disable the HTTP server feature on internet-facing systems. [KNOWN: Cisco advisory]

## ATT&CK techniques involved

- [T1190](https://attack.mitre.org/techniques/T1190/) Exploit Public-Facing Application
- [T1136](https://attack.mitre.org/techniques/T1136/) Create Account
- [T1505](https://attack.mitre.org/techniques/T1505/) Server Software Component

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- Turn off management web interfaces on devices that face the internet.
- Routers and switches need patching and monitoring just like servers.
- Check your router config for accounts you didn't create.

## Practice it

[Lab 2](../labs/02-harden-your-cisco-router.md). Your Cisco 1941 runs classic IOS, not IOS XE, so this exact bug doesn't apply, but the same lesson does: `no ip http server`. [INFERRED]

## Sources

- https://blog.talosintelligence.com/active-exploitation-of-cisco-ios-xe-software/
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxe-webui-privesc-j22SaA4z

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
