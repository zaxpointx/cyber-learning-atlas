# Where to find good cyber knowledge, and how to judge it

Answers issue #5. Checked 2026-11-22. Every link below was opened on that date.

Tags: [KNOWN] means the source says it. [INFERRED] means my reasoning. [UNKNOWN] means I looked and could not confirm.

## The short version

- The best free stuff lives in four places: top conference papers, artifact lists, talk archives, and DOE's OSTI. [INFERRED]
- Start any new topic with an **SoK paper**. It is a map of a whole field, written by researchers. [INFERRED]
- Prefer papers that earned an **artifact badge**. Someone outside the team ran their code. [KNOWN]
- Judge a GitHub project by recent pushes and its OpenSSF Scorecard, not by stars alone. [INFERRED]
- One newsletter a week is enough to stay current. [INFERRED]

## 1. Conference papers (the top four)

Security research has four "top" academic venues: USENIX Security, NDSS, IEEE S&P and ACM CCS. [INFERRED]
The tool top4grep calls them "the top 4 security conferences". [KNOWN] ([top4grep](https://github.com/Kyle-Kyle/top4grep))

### USENIX Security

- Good for: deep, practical systems and network research.
- Access: full proceedings and single papers download free, no login. [KNOWN] ([2025 program](https://www.usenix.org/conference/usenixsecurity25/technical-sessions))
- Some talks also have free video and slides. [KNOWN] (same page)
- How to search: open a year's "technical sessions" page and use your browser's find (Cmd+F) for a keyword. [INFERRED]
- Year list: [USENIX Security by year](https://www.usenix.org/conferences/byname/108).

### NDSS

- Good for: network and internet security.
- Access: NDSS says it gives "cost-free access to all abstracts, papers, posters, and presentations". [KNOWN] ([Why NDSS](https://www.ndss-symposium.org/why-ndss/))
- Talk videos are on YouTube. [KNOWN] (same page)
- How to search: the [paper archive](https://www.ndss-symposium.org/ndss-paper/) has a search box. [KNOWN]

### IEEE S&P (Oakland)

- Good for: big-picture research and the best SoK papers.
- Access: the official proceedings sit in IEEE's digital library. The accepted papers page lists titles only. [KNOWN] ([S&P 2025 accepted papers](https://sp2025.ieee-security.org/accepted-papers.html))
- Free route: IEEE lets authors post the accepted version on their own site, their school's repository, and arXiv. [KNOWN] ([IEEE post-publication policy](https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/post-publication-policies/))
- How to search: paste the exact title into a search engine plus "pdf", or search arXiv. [INFERRED]
- Watch out: some author copies are missing. Skip those rather than use a paywall. [INFERRED]

### ACM CCS

- Good for: applied crypto, web, and privacy work.
- Access: the ACM Digital Library became fully open access on 1 January 2026. Reading needs no subscription. [KNOWN] ([SMU library note](https://library.smu.edu.sg/topics-insights/acm-digital-library-now-fully-open-access))
- The paid "premium" tier adds tools like bulk download and citation tracking, not reading access. [KNOWN] (same page)
- I could not open ACM's own open access page (it blocked my request). [UNKNOWN]

### One tool to search all four

- **top4grep** is a small command line tool that greps paper titles from all four venues. [KNOWN]
- Example: `top4grep -k linux,kernel` finds titles with both words. [KNOWN]
- Limits: titles only, no abstracts, no OR searches yet. [KNOWN]
- Signals: 203 stars, last push June 2026, not archived. [KNOWN] (GitHub API, 2026-11-22)
- This is a lesser-known gem. It is not in research/README.md yet. [INFERRED]

## 2. SoK papers (your starting maps)

- SoK means "systematization of knowledge".
- IEEE S&P says an SoK paper should "provide an important new viewpoint on an established, major research area". [KNOWN] ([S&P 2026 call for papers](https://sp2026.ieee-security.org/cfpapers.html))
- They are judged on how well they organize past work, not on new results. A plain survey with no new insight does not qualify. [KNOWN] (same page)
- Titles start with "SoK:". That makes them easy to search. [KNOWN] (same page)

How to search:

- arXiv, security category, title contains SoK:
  `https://export.arxiv.org/api/query?search_query=ti:SoK+AND+cat:cs.CR`
- On 2026-11-22 that returned 297 results, newest first if you add `&sortBy=submittedDate`. [KNOWN]
- Recent examples: an SoK on LLMs in vulnerability research, one on attacks on agentic AI, one on post-quantum crypto adoption. [KNOWN]
- Better filter: search the title on the conference site too. An SoK accepted at S&P passed peer review. An arXiv-only one may not have. [INFERRED]

How to use one:

1. Read the abstract and the big table or diagram (most SoKs have one).
2. Pick two or three papers it cites as key.
3. Read those next. Now you have a reading path, not a random pile. [INFERRED]

## 3. Artifact-evaluated papers (research with runnable code)

This is the strongest quality signal in this whole file.

- **What it is:** a committee from outside the author team tries the paper's code and data. [KNOWN] ([USENIX Security 2025 call for artifacts](https://www.usenix.org/conference/usenixsecurity25/call-for-artifacts))
- **Badges:** Artifacts Available, Artifacts Functional, Results Reproduced. [KNOWN] ([secartifacts results 2024](https://secartifacts.github.io/usenixsec2024/results))
- **Available** means the code sits on a permanent archive like Zenodo or Software Heritage, not just a personal site. [KNOWN] (USENIX call)
- At USENIX Security 2025, sharing artifacts is the default. Functional and Reproduced checks are optional. [KNOWN] (USENIX call)

Where to browse:

- [secartifacts.github.io](https://secartifacts.github.io/) collects artifact results for ACSAC, CHES, NDSS, PETS, S&P, SysTEX, USENIX Security, VehicleSec and WOOT. [KNOWN]
- Its **ArtiFinder** pages also list code for papers that skipped evaluation, including ACM CCS. [KNOWN] (same page)
- Example: USENIX Security 2024 shows about 142 papers, 126 functional and 99 reproduced. [KNOWN] (results page)
- The Terrapin SSH attack paper earned all three badges plus a Distinguished Artifact Award. [KNOWN] (results page)
- The repo was last pushed 2026-11-12. It is actively kept. [KNOWN] (GitHub API)

Lab fit for your Mac mini:

- Many artifacts expect x86 Linux, big RAM, or GPUs. Read the artifact appendix first. [INFERRED]
- Never copy exploit code from an artifact into this repo. Link to it. (AGENTS.md rule 2)

## 4. Free talk archives

### DEF CON media server

- [media.defcon.org](https://media.defcon.org/) has folders for every DEF CON from 1 to 35, plus regional events. No login. [KNOWN]
- Inside each year: presentations, video and slides, villages and creators, workshops. [KNOWN] ([DEF CON 33 folder](https://media.defcon.org/DEF%20CON%2033/))
- How to search: open "presentations" for a year and Cmd+F a topic. Village folders are where beginner talks hide. [INFERRED]

### CCC media (Chaos Computer Club)

- [media.ccc.de](https://media.ccc.de/) holds about 17,500 recordings from 501 events. [KNOWN]
- Downloads include video, slide PDFs and subtitles. [KNOWN]
- Good for: deep technical talks from Europe's biggest hacker event (the yearly Congress, like 39C3). [KNOWN] (event list on the page)
- This one is new to the atlas. [INFERRED]

### Conference talk videos

- USENIX and NDSS talk videos are free (see section 1). [KNOWN]
- Black Hat archive page blocked my request. The YouTube channel in research/README.md is still the free route. [UNKNOWN]

## 5. OSTI.gov and DOE CODE (national lab research)

### OSTI.gov

- Run by the Department of Energy's Office of Scientific and Technical Information. [KNOWN] ([OSTI.gov](https://www.osti.gov/))
- Holds technical reports, journal articles, data, software, conference papers and video. [KNOWN]
- Example search: [cybersecurity intrusion detection](https://www.osti.gov/search/semantic:cybersecurity%20intrusion%20detection) gave 1,753 results. [KNOWN]

How to search it well:

- Tick **Full Text / Resource Available**. That hides citation-only records you cannot read. [KNOWN] (filter on results page)
- Filter by **Resource Type: Technical Report**. Lab reports are often more hands-on than journal papers. [INFERRED]
- Filter by **Research Organization** to see one lab, for example Sandia had 390 hits on that search. [KNOWN]
- Results export to CSV or JSON, up to 1,000 at a time. Handy for building atlas entries. [KNOWN]
- Grid and ICS security is where DOE labs are strongest. [INFERRED]

### DOE CODE

- [DOE CODE](https://www.osti.gov/doecode/) is DOE's search for software its funding paid for. [KNOWN]
- Use **Project Type: Open Source, Publicly Available Repository** to get code you can actually see. [KNOWN]
- You can also filter by license (MIT, Apache 2.0, GPL and more), language, and research organization. [KNOWN]
- This one is new to the atlas. [INFERRED]

Rule check: if any OSTI document carries a CUI, OUO or export marking, close it and do not use it. (AGENTS.md rule 7)

## 6. GitHub search that finds good projects

GitHub search qualifiers from the [official docs](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories). All [KNOWN].

| Qualifier | What it does |
|---|---|
| `topic:` | Repos tagged with a topic |
| `pushed:>2026-05-01` | Pushed recently |
| `stars:>200` | Some community use |
| `archived:false` | Not abandoned |
| `license:apache-2.0` | Has a clear license |
| `in:readme` | Word appears in the README |
| `good-first-issues:>2` | Has starter issues you could help with |

Example search for a maintained detection tool:

`topic:detection-engineering pushed:>2026-05-01 archived:false stars:>100`

Then check the project's OpenSSF Scorecard:

- Scorecard grades a project on checks like Maintained, Code-Review, Security-Policy, Signed-Releases and Pinned-Dependencies. [KNOWN] ([scorecard.dev](https://scorecard.dev/))
- You can read a score with no install. Open this in a browser, swapping in the repo:
  `https://api.securityscorecards.dev/projects/github.com/ossf/scorecard`
- That returned a score of 8.8 out of 10, dated 2026-11-21. [KNOWN]
- Not every repo has a published score. [INFERRED]

## 7. Curated lists

- The "awesome" lists are the classic curated lists on GitHub. [KNOWN]
- The main list has real rules: 30 days old, not AI generated, real effort, and no unmaintained or archived projects. [KNOWN] ([awesome list rules](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md))
- Security examples and their signals on 2026-11-22: [KNOWN] (GitHub API)
  - [awesome-security](https://github.com/sbilly/awesome-security): 15,142 stars, last push January 2026.
  - [awesome-pentest](https://github.com/enaqx/awesome-pentest): 27,821 stars, last push July 2026.
- A list being on the main awesome list is a decent signal. Being called "awesome" alone is not. [INFERRED]
- Lists are leads, not proof. Check each link they give you. [INFERRED]

## 8. Newsletters and feeds

- [tl;dr sec](https://tldrsec.com/): free, about weekly, archive is browsable. [KNOWN] Good for: a fast summary of the best new tools and talks. [INFERRED]
- [Detection Engineering Weekly](https://www.detectionengineering.net/archive): already in the atlas. Roughly weekly with breaks, last issue 12 Nov 2026. [KNOWN]
- arXiv cs.CR: already in the atlas. Preprints are not peer reviewed yet. [KNOWN] (research/README.md)

## 9. Checking if a paper matters

- [Semantic Scholar](https://www.semanticscholar.org/faq) shows citation counts and "Highly Influential Citations" without a login. [KNOWN]
- Influential citations are a model's guess, and full text is not always there, so counts can be off. [KNOWN] (same page)
- New papers have few citations. Do not punish a 2026 paper for that. [INFERRED]

## Quality signals (proposed bar for the atlas)

A find is worth a deep read if it hits **at least two** of these. [INFERRED, proposal]

1. **Primary.** Written by the people who did the work (the paper, the advisory, the repo), not a blog about it.
2. **Peer reviewed or official.** Accepted at a named venue, or published by a government or standards body.
3. **Reproducible.** Has an artifact badge, or public code and data you could run in a VM.
4. **Maintained.** For tools: a push in the last 6 months, not archived, and issues get answers.
5. **Scored.** For tools: OpenSSF Scorecard of 6 or more, if a score exists.
6. **Cited.** Other good sources point to it (citations, or an SoK lists it).
7. **Free and open.** Readable without login. Clear license.
8. **Fits your lab.** Runs on Apple Silicon or an ARM VM, or says clearly what it needs.

The numbers (2 of 8, 6 months, score 6) are my starting guesses, not a standard. Tune them when the atlas sets its bar. [INFERRED]

## Red flags (likely noise)

- No author, no date, or no sources.
- Repackages someone else's research without linking the original.
- "Ultimate", "100+ tools" or "complete guide" lists with no descriptions.
- A GitHub repo with lots of stars but no push in over a year, or archived.
- No license, or a README that is only a demo GIF.
- Asks for an email, login or download to read it.
- Claims a tool "hacks anything" or promises exploits.
- Looks AI generated: generic text, broken links, made-up citations.
- An arXiv preprint treated as settled fact.
- Old talk or paper on a topic that changes fast (cloud, AI), with no newer follow-up.

All red flags are [INFERRED] from the signals above.

## What is new compared with research/README.md

Already in the atlas: USENIX Security papers, DEF CON media server, Black Hat YouTube, arXiv cs.CR, Detection Engineering Weekly, OpenSSF Scorecard.

New in this file:

- NDSS, IEEE S&P and ACM CCS, and how to read each for free.
- The ACM Digital Library going fully open access in 2026.
- SoK papers, and a ready search for them.
- Artifact badges and secartifacts.github.io, plus ArtiFinder.
- top4grep, one search across all four top venues.
- media.ccc.de talk archive.
- OSTI.gov and DOE CODE, with filters that matter.
- GitHub search qualifiers and the no-install Scorecard lookup.
- Rules for judging awesome lists.
- tl;dr sec newsletter.
- Semantic Scholar for citation checks.
- A draft quality bar and red flag list.

## Gaps

- I could not open ACM's own open access page or Black Hat's archive. Both blocked automated requests. [UNKNOWN]
- I could not open dblp (bot protection), so it is not covered here. [UNKNOWN]
- I did not check every IEEE S&P paper for a free author copy. Some will be missing. [UNKNOWN]
