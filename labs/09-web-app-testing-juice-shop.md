# Lab 9: Hack a vulnerable web app you run yourself (OWASP Juice Shop)

**Goal:** see SQL injection and other common web bugs safely, and scan with ZAP.
**Time:** 2 to 4 hours. **Level:** beginner to intermediate.
**ATT&CK:** [T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/).
**Covers:** Security+ application attacks, OWASP Top 10.

## Safety

Juice Shop is insecure on purpose. Bind it to localhost only and never expose it to the internet.

## Setup

On `parrot` (or your Mac with Docker), the Juice Shop image has arm64 builds: [KNOWN: Docker Hub]

```bash
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

Open http://127.0.0.1:3000. Project page: https://owasp.org/www-project-juice-shop/

## Steps

1. **Find the score board.** It's hidden. Finding it is the first challenge.
2. **Log in as admin with SQL injection.** Try the login form. Ask your agent to explain *why* a single quote can break a SQL query, before trying the classic tricks.
3. **Scan it with ZAP:** `docker run --rm --network host zaproxy/zap-stable zap-baseline.py -t http://127.0.0.1:3000` and read the report. (On macOS Docker Desktop, use `http://host.docker.internal:3000` as the target instead.) [INFERRED: Docker networking differs by platform]
4. **Map what you found** to the [OWASP Top 10:2025](https://owasp.org/Top10/2025/) categories.
5. **Read the real version:** the [MOVEit incident](../incidents/moveit-cl0p-2023.md) was SQL injection in a real product.
6. **Go further:** the free [PortSwigger Web Security Academy](https://portswigger.net/web-security) SQL injection labs.

## Check yourself

- What's the real fix for SQL injection? (Hint: parameterized queries, not filtering quotes.)
- What did ZAP find that you didn't, and what did you find that ZAP missed?

## Write-up

Three challenges you solved, how, and the fix for each. Don't post full solutions to Juice Shop challenges publicly if you want to keep it fun for others; describe the bug class and the fix.
