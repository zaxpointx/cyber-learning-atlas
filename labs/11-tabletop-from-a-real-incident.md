# Lab 11: Run a tabletop exercise from a real incident

**Goal:** practice incident response decisions using a real case, no computers needed.
**Time:** 1 to 2 hours. **Level:** beginner.
**ATT&CK:** depends on the incident (see its page).
**Covers:** Security+ incident response, NIST SP 800-61 Rev. 3.

## Setup

Pick one: [SafePay ransomware](../incidents/safepay-2026.md), [Change Healthcare](../incidents/change-healthcare-2024.md) or [Colonial Pipeline](../incidents/colonial-pipeline-2021.md). Skim [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) for the response steps.

## Steps

1. **Ask your AI agent to run it.** Prompt: "Act as the facilitator for a tabletop exercise based on incidents/<file>.md in this repo. Give me one inject at a time, wait for my decision, then tell me what happened next and what the real organization did, citing only the sources listed."
2. **Build a timeline:** first access, first detection chance, ransomware or impact, recovery.
3. **Mark detection chances:** for each step, which log or tool from this repo could have caught it?
4. **Make the hard calls:** shut down systems or not? Who do you tell? Pay or not? (No right answer, but you have to explain your reasoning.)
5. **Lessons learned:** three changes you'd make, mapped to D3FEND defenses.

## Check yourself

- Where was the earliest point the attack could have been stopped?
- Which decision would you want made *before* an incident, not during?

## Write-up

Timeline, detection chances, your decisions, and three lessons. This is close to what a SOC analyst writes after a real incident. [INFERRED]
