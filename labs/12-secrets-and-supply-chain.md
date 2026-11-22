# Lab 12: Secrets and supply chain hygiene for your own repos

**Goal:** make sure your own GitHub repos (and your AI agents) never leak keys, and learn to check software you install.
**Time:** 1 to 2 hours. **Level:** beginner.
**ATT&CK:** [T1195 Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/), [T1552 Unsecured Credentials](https://attack.mitre.org/techniques/T1552/).
**D3FEND:** [Software Inventory](https://d3fend.mitre.org/technique/d3f:SoftwareInventory/), [Credential Rotation](https://d3fend.mitre.org/technique/d3f:CredentialRotation/).
**Covers:** Security+ secure development and supply chain risk.

## Why this lab

Read the [CISA GitHub leak](../incidents/cisa-github-leak-2026.md) and [XZ Utils](../incidents/xz-utils-2024.md) incidents first. One is secrets in a public repo; the other is a poisoned open-source package.

## Steps

### Part A: secrets

1. Install Gitleaks (https://github.com/gitleaks/gitleaks): `brew install gitleaks` on the Mac.
2. Scan your own repos, including their history: `gitleaks git <path-to-your-repo> -v` (older versions use `gitleaks detect --source <path>`; check `gitleaks --help`).
3. If anything real shows up: **rotate the secret first** (make a new key, revoke the old one), then clean the repo. Deleting the file isn't enough because git history keeps it.
4. Add a check before every commit with the [pre-commit](https://pre-commit.com/) framework and Gitleaks' hook, so you (or an agent) can't commit a key by accident.
5. Turn on GitHub secret scanning and push protection for your repos: https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning
6. Add a `.gitignore` line for `.env`, `*.pem` and `*.key` in every project.

### Part B: supply chain

1. Check the XZ version on your Parrot VM: `xz --version`. Versions 5.6.0 and 5.6.1 were the backdoored ones. [KNOWN: CISA alert]
2. Verify the Parrot ISO you downloaded: compare its `sha256sum` with the hash on Parrot's download page, and verify the signature if they provide one.
3. Look up one of your favorite open-source tools on https://scorecard.dev/ and read its security score.

## Check yourself

- Why rotate a leaked key even if you delete it a minute later?
- What could an AI coding agent do that leaks a secret, and how does a pre-commit hook stop it?

## Write-up

What Gitleaks found (redact real values), what you fixed, and your new pre-commit setup.
