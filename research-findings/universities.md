# University courses and labs for hands-on learning

Research for [issue #4](https://github.com/zaxpointx/cyber-learning-atlas/issues/4).
Checked on 2026-11-22. Every link below was opened that day.

Tags: **[KNOWN]** = stated on the source page. **[INFERRED]** = my reasoning. **[UNKNOWN]** = looked, not found.

## The short answer

- **Start with SEED Labs.** Free, no account, made by a university for exactly this. Most labs have an Apple Silicon version.
- **Do pwn.college next to it.** It runs in your browser, so the Mac doesn't matter. It needs a free account.
- **Read Berkeley's free CS 161 textbook** as the "why" behind both.
- **Save the x86 binary courses for later.** They are great, but slow or awkward on an ARM Mac.

## What v1 already covers, and the gap

The 12 labs in `labs/` are mostly **defender work with real tools**: scanning, hardening, logs, Zeek, Sigma, Wazuh, Atomic Red Team, Juice Shop.

What they don't teach yet:

- How network protocols break at the packet level (ARP, TCP, DNS spoofing).
- Applied crypto: why padding, keys, certificates and TLS go wrong.
- How programs work in memory: C, the stack, assembly, debugging.
- Reverse engineering.
- Writing secure code yourself and fixing flaws.
- Internet routing (BGP) and DNS as a whole system.

The university material below fills exactly those gaps. [INFERRED]

## Safety notes before you start

- Every lab here runs in **your own VM or the platform's own servers**. That fits rule 1 in AGENTS.md. [INFERRED]
- One project tells students to scan a public test server (Stanford CS155, see below). **Skip that part** or scan your own VM instead. The repo rule is own machines only.
- Course staff often ask you not to post solutions. Your write-ups should explain what you learned, not paste working attack code. That also keeps the repo within rule 2.

## Quick table

| # | Find | Free, no sign-up? | Apple Silicon | Level |
|---|---|---|---|---|
| 1 | SEED Labs (Syracuse) | Yes | Mostly yes | Beginner+ to intermediate |
| 2 | SEED Internet Emulator | Yes | Likely yes | Intermediate |
| 3 | pwn.college (ASU) | Free account | Yes (browser) | Beginner to advanced |
| 4 | CTF Primer (CMU CyLab) | Readable, yes | Yes (web) | Beginner |
| 5 | Berkeley CS 161 textbook | Yes | Yes (web) | Beginner+ |
| 6 | Berkeley CS 161 Project 1 | Yes (local VM) | Slow (emulated) | Intermediate |
| 7 | Stanford CS 155 projects | Yes | Likely yes | Intermediate |
| 8 | Stanford CS 253 Web Security | Yes (slides) | Yes | Intermediate |
| 9 | MIT 6.858 on OpenCourseWare | Yes | Videos yes, labs no | Advanced |
| 10 | MIT 6.5660 labs | Code yes, grading no | Slow (x86) | Advanced |
| 11 | Georgia Tech CS 6265 tutorials | Yes | x86 only | Advanced |
| 12 | CMU Bomb Lab and Attack Lab | Yes | x86 only | Intermediate |
| 13 | RPI Modern Binary Exploitation | Yes | x86 only | Intermediate to advanced |
| 14 | Helsinki Cyber Security Base | Free account | Yes | Beginner+ |
| 15 | UIUC SIGPwny meetings | Yes | Yes (slides, video) | Beginner to intermediate |
| 16 | angr | Yes | Unknown | Advanced |

Gems most people miss: **2, 4, 5, 7, 11, 15**.

---

## 1. SEED Labs (Syracuse University)

[seedsecuritylabs.org](https://seedsecuritylabs.org/)

**What it is.** Over 40 hands-on labs, started in 2002 by a Syracuse professor with NSF funding. Used by over a thousand schools. [KNOWN: home page and [GitHub README](https://github.com/seed-labs/seed-labs)]

**Free?** Yes. Task PDFs and setup files are direct downloads. No login shown. [KNOWN: [ARP lab page](https://seedsecuritylabs.org/Labs_20.04/Networking/ARP_Attack/)]
License is CC BY-NC-SA 4.0. [KNOWN: GitHub README]

**Apple Silicon.** Good, with gaps.

- The prebuilt VM is x86 VirtualBox and won't run on M-series Macs. [KNOWN: [lab setup page](https://seedsecuritylabs.org/labsetup.html)]
- The official fix is an ARM Ubuntu 22.04 VM in VMware Fusion. [KNOWN: [Apple ARM guide](https://github.com/seed-labs/seed-labs/blob/master/lab-setup/apple-arm/seedvm-fusion.md)]
- There are newer Ubuntu 24.04 build scripts (minimum 2 cores, 4 GB RAM, 10 GB disk). [KNOWN: [24.04 VM folder](https://github.com/seed-labs/seed-labs/tree/master/lab-setup/ubuntu24.04-vm)] Whether they run on ARM isn't stated. [UNKNOWN] The sister SEED Emulator repo does have an ARM 24.04 build folder (see find 2). [KNOWN]
- Labs ship a `Labsetup-arm.zip` "for Apple Silicon machines." [KNOWN: ARM lab page]
- UTM should work too, since it's just an ARM Ubuntu VM plus Docker. SEED doesn't test UTM. [INFERRED]

From SEED's own [ARM test results](https://github.com/seed-labs/seed-labs/blob/master/lab-setup/apple-arm/Lab_Testing.md) [KNOWN]:

- **Works:** Sniffing/Spoofing, ARP, ICMP Redirect, DNS Local and Remote, Firewall, VPN, XSS, CSRF, SQL Injection, Set-UID, Shellshock, Format String, most crypto labs (secret key, padding oracle, hash, RSA, PKI, TLS).
- **Partly:** TCP, DNS Rebinding, BGP.
- **Not on ARM:** Buffer Overflow (setuid), Return-to-libc, Dirty COW, Heartbleed, Meltdown, Spectre, Random Number.

**Level.** Beginner+ to intermediate. Each lab says about 2 hours guided, or a week as homework. [KNOWN: ARM lab page]

**What it adds to v1.** Packet-level network attacks, web flaws from the inside, and real crypto mistakes. This is the biggest gap filler on this list. [INFERRED]

**How to work through it.**

1. Build an Ubuntu 22.04 ARM VM in UTM, following SEED's Apple ARM guide but with UTM instead of Fusion. Give it 4 GB RAM and 2 cores. [INFERRED]
2. Install SEED's lab software from that guide and use the `Labsetup-arm.zip` files. Keep it on the isolated lab network from Lab 0.
3. Do these in order: Sniffing/Spoofing, ARP, TCP, DNS Local, Firewall, VPN.
4. Then XSS, CSRF, SQL Injection (pairs with Lab 9).
5. Then Secret-Key, Padding Oracle, RSA, PKI, TLS.
6. One write-up per lab, same template as v1.

---

## 2. SEED Internet Emulator (Syracuse)

[github.com/seed-labs/seed-emulator](https://github.com/seed-labs/seed-emulator)

**What it is.** A Python tool that builds a small fake Internet out of Docker containers: autonomous systems, BGP routers, DNS servers, exchanges. Some examples draw a live map in your browser. [KNOWN: README]

**Free?** Yes, GPL-3.0. Installs with pip. Needs Python 3.10+ and Docker. [KNOWN: README]

**Apple Silicon.** The repo includes an ARM VM build folder (`VM_images/SeedVM24.04/src-arm`). [KNOWN: repo tree] The README itself has no ARM notes. [UNKNOWN: whether every example image runs on ARM]

**Level.** Intermediate.

**What it adds.** How the Internet actually routes, and how BGP and DNS fail at scale. Nothing in v1 touches this. **Lesser-known gem.** [INFERRED]

**How to work through it.** Do the SEED BGP and DNS Infrastructure labs first, then run the `A00-simple-as` and `B02-mini-internet-with-dns` examples and change one thing at a time.

---

## 3. pwn.college (Arizona State University)

[pwn.college](https://pwn.college/)

**What it is.** ASU's hacking curriculum, open free to anyone. Organized as "dojos" with belts from white to black. [KNOWN: home page, [dojos page](https://pwn.college/dojos)]

**Free?** Free, but **needs a free account** to save progress and earn belts. [KNOWN: Register and Login links; belts need the account email]

**Apple Silicon.** Doesn't matter. Each challenge opens a browser terminal, VS Code in the browser, a full Linux desktop in the browser, or SSH. [KNOWN: [Using the Dojo module](https://pwn.college/welcome/welcome/)]

**Level.** Beginner (Linux) to very advanced (kernel and exploitation).

**What it adds.**

- [Linux Luminarium](https://pwn.college/linux-luminarium/): 17 modules on paths, pipes, permissions, processes. Deeper than OverTheWire Bandit. [KNOWN]
- [Computing 101](https://pwn.college/computing-101/): memory, the stack, assembly, debugging. [KNOWN]
- [Intro to Cybersecurity](https://pwn.college/intro-to-cybersecurity/): web, intercepting traffic, crypto, access control, reverse engineering, binary exploitation. [KNOWN]

It's already listed in `practice/`, but as "great later on." I'd move Linux Luminarium up to "now." [INFERRED]

**How to work through it.** Welcome module, then Linux Luminarium, then Computing 101, then Intro to Cybersecurity (orange belt). One module a week. There's an AI helper called SENSAI if you get stuck. [KNOWN: welcome module]

---

## 4. The CTF Primer (Carnegie Mellon CyLab)

[primer.picoctf.org](https://primer.picoctf.org/)

**What it is.** A free online book from the picoCTF team (now CyLab Security Academy). Chapters: the shell, forensics, Python, web exploits, crypto, networking, databases, C, assembly, binary exploitation. Plus a careers appendix. [KNOWN]

**Free?** The page loads without logging in. It recommends a free CyLab Academy account for the web shell and challenges. [KNOWN] The academy says signing up is free. [KNOWN: [learners page](https://cylabacademy.org/learners.html)]

**Apple Silicon.** Web only, so yes.

**Level.** Beginner. Written for high schoolers. [INFERRED from the picoCTF audience]

**What it adds.** The reading that goes with the picoCTF puzzles already in `practice/`. Most people skip straight to the puzzles and get stuck. **Lesser-known gem.** [INFERRED]

**How to work through it.** Read one chapter, then solve three challenges on that topic in the Challenge Library.

---

## 5. Berkeley CS 161 online textbook

[textbook.cs161.org](https://textbook.cs161.org/) (source on [GitHub](https://github.com/cs161-staff/textbook))

**What it is.** UC Berkeley's free textbook for its intro security course. Units: security principles, memory safety, cryptography, web, network. A full PDF is in the repo. [KNOWN: repo contents and search listing]

**Free?** Yes, no sign-up. Repo updated October 2026. [KNOWN: GitHub]

**Apple Silicon.** Web, so yes.

**Level.** Beginner+ (college sophomore level, but clearly written). [INFERRED]

**What it adds.** The clearest free explanation I found of *why* memory bugs and crypto mistakes happen. Pair each chapter with the matching SEED lab. **Lesser-known gem.** [INFERRED]

Note: the site didn't resolve from my network during this check, so I verified it through the GitHub repo. [KNOWN]

---

## 6. Berkeley CS 161 Project 1 (memory safety)

[Fall 2025 Project 1](https://inst.eecs.berkeley.edu/~cs161/fa25/proj1/getting-started/)

**What it is.** A series of puzzles against a deliberately weak program in a VM, reached over SSH. [KNOWN]

**Free?** The local VM download is linked on the page. [KNOWN] Grading needs a Berkeley account. [INFERRED]

**Apple Silicon.** The page says "students with M1 Macs can only use the QEMU setup," which emulates x86-64. Works, but slower. [KNOWN]

**Level.** Intermediate.

**What it adds.** The stack and memory bugs that SEED can't run on ARM. A good ARM-friendly fallback for those labs. [INFERRED]

Lecture playlist is public on YouTube, linked from the [course home](https://inst.eecs.berkeley.edu/~cs161/fa25/). [KNOWN]

---

## 7. Stanford CS 155 projects (Spring 2026)

[cs155.stanford.edu](https://cs155.stanford.edu/)

**What it is.** Stanford's main security course. Project handouts and starter code are public. [KNOWN]

- **Project 2, Web:** attack and then defend a small Node.js app ("Bitbar") in a Docker container. Cookie theft, cross-site attacks, then fixes. [KNOWN: [handout PDF](https://cs155.stanford.edu/hw_and_proj/proj2/proj2_handout.pdf)]
- **Project 3, Network:** Nmap, Wireshark, write a scan detector in Go, then a DNS spoofing "monster in the middle" in Docker. [KNOWN: [handout PDF](https://cs155.stanford.edu/hw_and_proj/proj3/proj3.pdf)]

**Free?** Yes, direct PDF and zip downloads. Grading is through Gradescope for students. [KNOWN]

**Apple Silicon.** Docker, Go, Nmap and Wireshark all run on M-series Macs. [INFERRED] The handouts don't mention ARM. [UNKNOWN]

**Safety flag.** Part 1 of Project 3 scans a public server. **Scan your own VM instead.** That's the repo rule.

**What it adds.** Both attack and defense on the same app, and writing your own detector. That's the step past running Zeek. **Lesser-known gem.** [INFERRED]

**How to work through it.** After Lab 9 (Juice Shop), do Project 2. After Lab 5 (Zeek), do Project 3 parts 2 to 4.

---

## 8. Stanford CS 253 Web Security (Fall 2021)

[web.stanford.edu/class/cs253](https://web.stanford.edu/class/cs253)

**What it is.** A whole course on how browsers and web apps get attacked and defended. Slides and past exams are linked openly. Five assignments. [KNOWN]

**Free?** Slides yes. Videos are not mentioned. [UNKNOWN: video access]

**Apple Silicon.** Yes, it's web dev.

**Level.** Intermediate. Expects some web programming. [KNOWN: prerequisites]

**What it adds.** Browser security concepts in depth (same-origin policy, cookies, CSP). Good companion to PortSwigger. It's from 2021, so some browser details have changed. [INFERRED]

---

## 9. MIT 6.858 Computer Systems Security (OpenCourseWare, 2014)

[ocw.mit.edu course page](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/)

**What it is.** A graduate security course: 22 video lectures, notes, exams, and 6 labs. [KNOWN: [videos](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/video_galleries/video-lectures/), [labs](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/pages/labs/)]

**Free?** Yes, no sign-in, CC BY-NC-SA 4.0. [KNOWN]

**Apple Silicon.** Videos, yes. Labs use an old VMware VM. [KNOWN] Expect it not to run well on ARM. [INFERRED]

**Level.** Advanced.

**What it adds.** How systems are *designed* to be secure: threat models, privilege separation, sandboxing. Watch the lectures, skip the labs. [INFERRED]

## 10. MIT 6.5660 labs (2023)

[css.csail.mit.edu/6.5660/2023](https://css.csail.mit.edu/6.5660/2023/)

The newer version of 6.858. Labs: buffer overflows, privilege separation, symbolic execution, browser security, WebAuthn. [KNOWN] Lab code is on [GitHub](https://github.com/mit-pdos/6.5660-lab-2023). [KNOWN: lab 1 page]

Apple Silicon: the course VM is x86-64, and on M1 or M2 Macs running it locally "may be prohibitively slow." [KNOWN: [lab 1](https://css.csail.mit.edu/6.5660/2023/labs/lab1.html)] Their fix is a paid cloud VM. Park this one. [INFERRED]

---

## 11. Georgia Tech CS 6265 tutorials

[tc.gts3.org/cs6265/tut](https://tc.gts3.org/cs6265/tut/)

**What it is.** 17 tutorials on binary hacking: GDB, Ghidra, shellcode, format strings, ROP, heap bugs, fuzzing, symbolic execution. [KNOWN]

**Free?** Yes. The page says anyone not enrolled can download the tutorials and run them in a local Vagrant VM. [KNOWN]

**Apple Silicon.** The binaries are 32-bit x86. [INFERRED from the addresses and registers on the first tutorial] You'd need an emulated x86 VM. Slow. [INFERRED]

**Level.** Advanced.

**What it adds.** The best-organized free path into reverse engineering and fuzzing that I found. **Lesser-known gem** for later. [INFERRED]

---

## 12. CMU Bomb Lab and Attack Lab (CS:APP)

[csapp.cs.cmu.edu/3e/labs.html](https://csapp.cs.cmu.edu/3e/labs.html)

**What it is.** The famous labs from CMU's systems course. Bomb Lab: defuse a program by reading its assembly. Attack Lab: stack attacks on practice targets. [KNOWN]

**Free?** Self-study handouts download directly (the bomb file returned a real tar file). [KNOWN: tested download] Solutions are instructor-only. [KNOWN]

**Apple Silicon.** Linux x86-64 binaries only. [KNOWN] Needs an emulated x86 VM. [INFERRED]

**Level.** Intermediate.

**What it adds.** The classic first taste of reverse engineering. Fun, and a common interview story. [INFERRED]

---

## 13. RPI Modern Binary Exploitation (2015)

[github.com/RPISEC/MBE](https://github.com/RPISEC/MBE)

**What it is.** A student-run Rensselaer course: 15 lecture slide sets, 10 labs, a wargame VM. [KNOWN]

**Free?** Yes. Slides CC BY-NC 4.0, code BSD. [KNOWN]

**Apple Silicon.** No. Ubuntu 14.04 32-bit VM. [KNOWN] Last pushed 2021. [KNOWN: GitHub]

**Level.** Intermediate to advanced. Assumes C and some assembly. [KNOWN]

**Notes.** The VM uses published default passwords, so never put it on a real network. Maintainers ask you not to post solutions. [KNOWN] Old but still a classic. Use the slides even if you skip the VM. [INFERRED]

---

## 14. University of Helsinki Cyber Security Base

[cybersecuritybase.mooc.fi](https://cybersecuritybase.mooc.fi/)

**What it is.** A free course series. Part 1: build web software, find its flaws, fix them. Part 2: crypto, network security, an intrusion prevention system, pen testing, and a final CTF. [KNOWN: [descriptions](https://cybersecuritybase.mooc.fi/descriptions)]

**Free?** Yes, free for everyone. Uses a mooc.fi account. [KNOWN: free; INFERRED: account, from the login links]

**Dates.** Part 1 runs 7 Sep to 13 Dec 2026. Part 2 runs 18 Jan to 9 May 2027. [KNOWN] So Part 2 is a good target for January.

**Apple Silicon.** Python based. [KNOWN: install guide link] Should be fine. [INFERRED]

**Level.** Beginner+. Needs some programming. [KNOWN]

**What it adds.** Writing secure code yourself, not just attacking. Nothing in v1 does this. [INFERRED]

---

## 15. UIUC SIGPwny meeting slides

[sigpwny.com/meetings](https://sigpwny.com/meetings/)

**What it is.** The University of Illinois security club's weekly meetings. Many have slides and YouTube recordings: web hacking, reverse engineering, pwn, crypto, OSINT, x86-64, Linux privilege escalation. [KNOWN]

**Free?** Yes for slides and YouTube. Some recordings are on Zoom and may need a school login. [KNOWN]

**Level.** Beginner to intermediate. Made by students for students.

**What it adds.** Short, friendly intros before a hard topic. **Lesser-known gem.** [INFERRED]

The official UIUC course pages (CS 461 / ECE 422) list topics but no public assignments. [UNKNOWN: public machine problems]

---

## 16. angr (research tool)

[angr.io](https://angr.io/) and [docs](https://docs.angr.io/en/latest/)

**What it is.** An open-source Python framework for analyzing programs automatically: symbolic execution, finding paths through code, even building ROP chains. BSD license, Python 3.12+. Used in research and CTFs. [KNOWN]

It grew out of university security labs. The site now says "researchers and hackers around the world." [KNOWN for the quote; UNKNOWN: the site doesn't name the founding labs]

**Apple Silicon.** [UNKNOWN] The docs page I read doesn't say.

**Level.** Advanced. Save this until after Georgia Tech or pwn.college orange belt.

---

## Checked and left out

- **MIT 6.5660 2025 page:** 404. The 2023 page is current. [KNOWN]
- **OpenSecurityTraining2:** didn't resolve from my network, and it's a nonprofit, not a university. Worth checking separately. [UNKNOWN]
- **SEED prebuilt VM:** x86 VirtualBox only. Build your own ARM VM instead. [KNOWN]

## Suggested order for you

1. Now, alongside Security+: pwn.college Linux Luminarium, the CTF Primer, Berkeley textbook chapters.
2. After v1 Lab 4: SEED network labs on an ARM VM.
3. After v1 Lab 9: SEED web labs, then Stanford CS155 Project 2.
4. After v1 Lab 5: Stanford CS155 Project 3 (skip the public scan), then SEED Emulator.
5. January 2027: Helsinki Cyber Security Base Part 2.
6. Later: pwn.college Computing 101 and Intro to Cybersecurity, then the x86 binary courses.

[INFERRED: the order is my judgment]
