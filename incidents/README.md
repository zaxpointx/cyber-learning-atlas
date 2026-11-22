# Incidents in plain words

Real attacks (and one big accident), explained simply: what happened, how they got in, what went wrong, and what you can practice. Every claim links to a public post-mortem, government advisory or sworn testimony.

**Key takeaway:** read five of these and you'll see the same few mistakes over and over: a login without MFA, an unpatched internet-facing device, and nobody watching the logs. That pattern is the whole point.

| Year | Incident | What it teaches | Level |
|---|---|---|---|
| 2015 | [Ukraine power grid attack](ukraine-grid-2015.md) | Business IT and grid control networks need hard separation. | intermediate |
| 2017 | [Equifax breach](equifax-2017.md) | Patch internet-facing systems fast, especially when a fix is public. | beginner |
| 2020 | [SolarWinds Orion supply chain attack (SUNBURST)](solarwinds-sunburst-2020.md) | A trusted vendor update is not proof of safety if the vendor itself is hacked. | intermediate |
| 2021 | [Colonial Pipeline ransomware](colonial-pipeline-2021.md) | One old account without MFA can take down critical infrastructure. | beginner |
| 2021 | [Log4Shell (Log4j)](log4shell-2021.md) | Keep a software bill of materials (SBOM): a list of what's inside your software. | beginner |
| 2022 | [Lapsus$ extortion attacks](lapsus-2022.md) | Text-message MFA is better than nothing but is weak. Use an authenticator app or a security key. | beginner |
| 2023 | [MOVEit Transfer mass data theft (Cl0p)](moveit-cl0p-2023.md) | File transfer servers hold sensitive data and face the internet: prime targets. | beginner |
| 2023 | [Cisco IOS XE web UI mass exploitation](cisco-ios-xe-2023.md) | Turn off management web interfaces on devices that face the internet. | beginner |
| 2023 | [Microsoft Exchange Online intrusion (Storm-0558)](storm-0558-2023.md) | Signing keys are crown jewels. Rotate them and protect them in hardware. | intermediate |
| 2024 | [Volt Typhoon pre-positioning in U.S. critical infrastructure](volt-typhoon-2024.md) | Normal admin tools used at strange times or from strange places are the signal. You need a baseline of normal. | intermediate |
| 2024 | [Change Healthcare ransomware](change-healthcare-2024.md) | Same lesson as Colonial Pipeline, three years later: one internet-facing login without MFA. | beginner |
| 2024 | [XZ Utils backdoor](xz-utils-2024.md) | Curiosity about small weird things saves the day. Investigate the odd slowdown. | intermediate |
| 2024 | [CrowdStrike faulty update outage (not an attack)](crowdstrike-outage-2024.md) | Availability is part of security (the A in the CIA triad). | beginner |
| 2024 | [Snowflake customer data theft (UNC5537)](snowflake-customers-2024.md) | Cloud accounts need MFA just like VPNs. | beginner |
| 2025 | [Salt Typhoon and telecom router compromises](salt-typhoon-2025.md) | Routers are computers, and attackers live on them for years. | intermediate |
| 2026 | [CISA credentials leaked in a contractor's public GitHub repo](cisa-github-leak-2026.md) | Never put secrets (keys, passwords, tokens) in a repo, even a "temporary" one. | beginner |
| 2026 | [SafePay ransomware](safepay-2026.md) | Edge devices and backup servers are top targets. Patch the KEV entries for them first. | beginner |

## The big yearly reports

See [yearly-reports.md](yearly-reports.md) for the Verizon DBIR, Mandiant M-Trends and other yearly reports, with the numbers that matter.

## How to add one

Follow [AGENTS.md](../AGENTS.md) section 4. Good sources: CISA advisories (https://www.cisa.gov/news-events/cybersecurity-advisories), CSRB reports, company post-mortems, court records and congressional testimony. Skip news stories that don't link a primary source.
