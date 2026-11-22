# The big yearly reports

These reports look at thousands of real incidents each year. Read the summaries below first, then skim the real thing. Numbers are from the reports' own public pages. [KNOWN unless marked]

## Verizon Data Breach Investigations Report (DBIR) 2026

Covers incidents from Nov 1, 2024 to Oct 31, 2025: more than 31,000 incidents and 22,000 confirmed breaches. Free to read. [KNOWN: DBIR 2026 report and press release]

- **Exploiting vulnerabilities is now the #1 way in (31%)**, ahead of stolen credentials (13%). First time in the report's 19 years.
- **Patching is slipping:** only 26% of KEV vulnerabilities were fully fixed, median 43 days.
- **Ransomware was in 48% of breaches**, but 69% of victims didn't pay. Median payment was about $140,000.
- **Third parties were involved in 48% of breaches**, up 60%.
- **Phone and text scams beat email:** mobile-style social engineering got about 40% more clicks than email phishing in simulations.
- **AI:** attackers used generative AI to help with known techniques (a median of 15 techniques per actor), mostly speeding up attacks defenders already know how to detect.

Sources: https://www.verizon.com/about/news/breach-industry-wide-dbir-finds and https://www.verizon.com/business/resources/reports/dbir/

**What this means for you:** patching (KEV), MFA, and watching third-party access are the three skills the data keeps pointing to.

## Mandiant M-Trends 2026

Based on Mandiant's incident response work in 2025. [KNOWN: Google Cloud blog post on M-Trends 2026]

- **Median dwell time rose to 14 days** (from 11). Dwell time is how long attackers are inside before being found.
- **Exploits were the top way in for the sixth year (32%).** Voice phishing jumped to second place (11%), and email phishing fell to 6%.
- Espionage cases and North Korean fake IT worker cases had much longer dwell times (median 122 days).

Sources: https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026 and https://cloud.google.com/security/resources/m-trends

## CISA KEV, by our own count

Not a report, but the best free "what's being exploited" data. See [techniques/kev.md](../techniques/kev.md). On 2026-11-22: 1,790 entries, 361 tied to ransomware. [KNOWN: our count from the CISA feed]

## Others worth knowing about

| Report | Why read it | Access |
|---|---|---|
| CISA #StopRansomware advisories | Group-by-group playbooks with ATT&CK tables | Free: https://www.cisa.gov/stopransomware |
| CISA Cybersecurity Advisories | Every joint advisory, newest first | Free: https://www.cisa.gov/news-events/cybersecurity-advisories |
| ENISA Threat Landscape | Europe's yearly overview | Free: https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape |

Some vendor reports (for example CrowdStrike's yearly threat report) ask for your email before download. Under this repo's rules we don't sign up for those. Read their public press summaries instead. [KNOWN: repo rule]

## Pattern across all of them

**Key takeaway:** the same three things show up every year. Attackers get in through internet-facing bugs or stolen logins, they live on the network for days to months, and backups and logs decide how bad it gets. [INFERRED from the reports above]
