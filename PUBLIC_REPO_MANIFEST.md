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
- buildable Odra Casper proof receipt registry with `Cargo.toml`, `Odra.toml`, `Cargo.lock`, `rust-toolchain`, build bins, and `src/proof_receipt_registry.rs`
- compiled `contract/wasm/ProofReceiptRegistry.wasm`
- judging and submission docs
- deterministic submission payload generator
- non-secret Casper CLI command template generator
- final readiness checker
- Japanese user Testnet action guide
- final submission checklist

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
npm run payload
npm run casper:commands
npm run readiness
```

`npm run readiness` is expected to return `needs_more_evidence` until the Casper Testnet contract/package hash and `record_proof_receipt` transaction hash are filled.

Wasm build verified in WSL:

```text
contract/wasm/ProofReceiptRegistry.wasm
sha256: 1a9add6be7dfc1dd2023c1c752fbc252890db22c0415adb137fd9e3c8a19bbcf
```

Status: public repo/demo/payload/Wasm ready; Testnet deploy and final DoraHacks submission still require user-controlled account actions.
