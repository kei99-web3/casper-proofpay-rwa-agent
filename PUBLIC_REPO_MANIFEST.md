# Public Repo Manifest

Repository: `casper-proofpay-rwa-agent`

URL: https://github.com/kei99-web3/casper-proofpay-rwa-agent

Demo URL: https://kei99-web3.github.io/casper-proofpay-rwa-agent/

Draft video URL: https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-draft.mp4

Purpose: public candidate repository for the Casper Agentic Buildathon 2026.

## Included

- dependency-free Node.js proof engine
- tests
- static demo
- short draft demo video
- MCP-style tool schemas
- x402-shaped payment flow mock
- Odra-style Casper proof receipt registry scaffold
- judging and submission docs

## Excluded

- private workspace context
- `.company/`
- secrets, tokens, private keys, wallet files, `.env`
- customer/outreach data
- unrelated Hedera/Tether/Sui/BOT/LCA/App Studio files
- generated automation/Telegram/Command Center reports

## Current Verification

Run:

```bash
npm test
npm run demo
```

Status: local candidate ready for review; Testnet deploy and final DoraHacks submission still require user-controlled account actions.
