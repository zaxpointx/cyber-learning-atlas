# Lab safety rules

Read this before every lab. These rules keep the labs legal and keep your real stuff safe.

## The law, in one paragraph

In the U.S., accessing or attacking a computer without permission can be a crime under the Computer Fraud and Abuse Act, even if you "were just testing". Permission means the owner said yes, in writing, for that exact system. For these labs, the only systems you have permission for are the ones you own. [KNOWN: this is the general rule; not legal advice]

## Rules

1. **Own machines only.** Your Mac, your VMs, your Cisco router. Not school, not TCAT, not your family's other devices, not your ISP, not a website.
2. **Isolated lab network.** Attack and scan traffic stays on a UTM "Host Only" network (or a separate cable to your router). Never on your home Wi-Fi network with other people's devices.
3. **Clone before you break.** Clone or back up the VM before any risky lab, so you can roll back.
4. **No real malware.** Use the EICAR test string and Atomic Red Team tests. Never download real malware samples.
5. **Read before you run.** Never paste a command you don't understand. Ask your agent to explain it line by line first.
6. **No public exposure.** Never port-forward a lab VM or a vulnerable app (like Juice Shop) to the internet.
7. **Old gear stays inside.** Your Cisco 1941 no longer gets security fixes (see Lab 2). Use it as a lab router, never as the router between your home and the internet.
8. **Practice platforms are separate.** Hack The Box, TryHackMe and the rest give you their own targets. Use their VPN or browser machine and follow their rules.

## If something goes wrong

- If a scan or test accidentally leaves your lab network, stop it, note what happened, and fix your network setup before continuing.
- If you think something you don't own was touched, tell an adult or your instructor. Being upfront is always the right move.
