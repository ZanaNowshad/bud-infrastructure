# Hermes Risk Register

| ID | Category | Description | Likelihood | Impact | Mitigation | Approval |
|----|----------|-------------|------------|--------|------------|----------|
| R001 | Secret leakage | API key exposed in logs/git/chat | Medium | Critical | .gitignore, env files excluded, no secrets in logs | N/A |
| R002 | Wallet compromise | Private key exposed | Low | Critical | Keys in encrypted file, never shared | N/A |
| R003 | API abuse | Rate-limited or suspended | Low | High | Retry with backoff, stay within limits | N/A |
| R004 | Excessive permissions | Tool granted more access than needed | Medium | High | Request minimum scope, prefer read-only | User |
| R005 | Tool supply-chain | Malicious package installed | Low | Critical | Pin versions, audit deps, official sources | N/A |
| R006 | Cloud misconfiguration | Sensitive data exposed | Low | High | Restrict sharing, private by default | User |
| R007 | Unauthorized financial action | Accidental transfer/trade | Low | Critical | Never execute without explicit approval | User |
| R008 | Tax/reporting failure | Missing crypto records | Medium | Medium | Log all activity, retain records | User |
| R009 | Affiliate disclosure failure | Non-compliant links | Low | Medium | Clear disclosure on all affiliate content | N/A |
| R010 | Platform ban | ToS violation | Low | High | Follow platform terms, no spam/abuse | N/A |
| R011 | Content quality violation | AI-generated spam | Medium | Medium | Human review gate for published content | User |
| R012 | Smart-contract loss | DeFi exploit | Low | Critical | Only audited, battle-tested protocols | User |
| R013 | Phishing | Fake site compromises credentials | Low | Critical | URL verification, 2FA | Both |
| R014 | Account takeover | Service account compromised | Low | Critical | Enable MFA on all accounts | User |
| R015 | Data loss | Files deleted | Medium | Medium | Git version control, backup | N/A |
| R016 | Automation loop failure | Infinite script | Low | High | Max 3 retries, iteration cap, escalate | N/A |
| R017 | Reputational damage | Agent behavior reflects poorly | Medium | High | Approval gates for public actions | User |
