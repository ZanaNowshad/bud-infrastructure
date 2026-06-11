# BUd Autonomy Protocols

## 1. Authentication Methods

| Service | Auth Type | Status |
|---------|-----------|--------|
| AgentMail | API Key (Bearer token in header) | Awaiting key |
| GitHub | OAuth token (via MCP integration) | Available (user: ZanaNowshad) |
| Crypto wallets | Private key (self-custodied) | Generated |
| Google Drive | OAuth 2.0 (via agentgate or direct) | Pending user choice |
| Payment APIs | API Key / OAuth | Not configured |

## 2. Required Credentials Checklist

To reach full autonomy, I need the following from you:

- [ ] **AgentMail API Key** — from console.agentmail.to (for agent email)
- [ ] **Cloud storage preference** — Google Drive, OneDrive, or local-only
- [ ] **Any exchange API keys** — if you want me to interact with centralized exchanges
- [ ] **AI service API keys** — for autonomous content generation (optional)

## 3. Error Handling Protocol

```
Task Execution Flow:
  1. Attempt the task with available credentials
  2. On success → log outcome, proceed to next task
  3. On auth failure → check if credentials exist
     a. If missing → log required credential → escalate to user
     b. If present but invalid → log error → request refresh
  4. On API/service failure → retry up to 2 times with exponential backoff
  5. On persistent failure → log full error + context → escalate
  6. On partial success → log what succeeded and what failed
```

### Retry Policy
- **Transient errors** (timeouts, rate limits): Retry after 2s, then 8s
- **Auth errors** (401, 403): Do not retry — escalate immediately
- **Server errors** (500+): Retry once after 5s
- **Client errors** (400, 404): Log and escalate

### Escalation Channels
- Primary: Report to user in chat with structured error details
- Fallback: Append to `logs/errors.log` with full context

## 4. Operational Rules

1. **Never commit .env or private keys to version control**
2. **Log every significant action** with timestamp and outcome
3. **Ask before spending money** (API costs, gas fees, subscriptions)
4. **Keep wallet private keys offline** — never paste into web forms
5. **Use testnet first** when exploring new DeFi/crypto protocols
6. **Report failures transparently** — log the error, don't hide it
