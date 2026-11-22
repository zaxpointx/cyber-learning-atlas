# SolarWinds Orion supply chain attack (SUNBURST) (2020)

**Topic:** supply-chain  
**Level:** intermediate  
**Last checked:** 2026-11-22

## What happened

In December 2020 it came out that attackers had compromised SolarWinds Orion, network monitoring software used across the federal government and big companies, so that its software updates carried a backdoor. CISA issued an emergency directive in response. [KNOWN: CISA ED 21-01; GAO-22-104746]

## How they got in and what went wrong

- A threat actor was in SolarWinds' networks as early as January 2019, according to the company's CEO, and the U.S. government later named Russia's Foreign Intelligence Service as responsible. [KNOWN: GAO-22-104746]
- Because Orion was widely used to monitor and manage federal networks, the compromised software let the attackers breach several federal agencies. [KNOWN: GAO-22-104746]
- CISA ordered agencies to disconnect or power down affected Orion products. [KNOWN: ED 21-01]
- Agencies later said evidence collection was limited because agencies kept different amounts of log data. [KNOWN: GAO-22-104746 lessons]

## ATT&CK techniques involved

- [T1195](https://attack.mitre.org/techniques/T1195/) Supply Chain Compromise
- [T1071](https://attack.mitre.org/techniques/T1071/) Application Layer Protocol
- [T1078](https://attack.mitre.org/techniques/T1078/) Valid Accounts

Mapping: [INFERRED] our reading of the sources, using ATT&CK v20.1 names. Advisories from CISA often include their own official mapping; check the source for theirs.

## Lessons

- A trusted vendor update is not proof of safety if the vendor itself is hacked.
- Monitoring tools have huge access, which makes them prime targets.
- Keep your logs. Investigators were held back where agencies hadn't preserved enough data.

## Practice it

[Lab 12](../labs/12-secrets-and-supply-chain.md) (supply chain basics) and [Lab 5](../labs/05-network-sensor-zeek-suricata.md) (spotting odd outbound traffic).

## Sources

- https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise
- https://www.gao.gov/products/gao-22-104746

Some government sites (like gao.gov) block automated link checkers. If a link fails in CI but opens in a browser, it is fine.
