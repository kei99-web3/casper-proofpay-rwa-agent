# Public Repo Manifest

Repository: `casper-proofpay-rwa-agent`

URL: https://github.com/kei99-web3/casper-proofpay-rwa-agent

Demo URL: https://kei99-web3.github.io/casper-proofpay-rwa-agent/

Final video URL: https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-final.mp4

Purpose: public candidate repository for the Casper Agentic Buildathon 2026.

## Included

- dependency-free Node.js proof engine
- tests
- static demo
- final demo video with Casper Testnet evidence
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

`npm run readiness` returns `ready_to_submit_after_user_approval` after the Casper Testnet contract/package hash and `record_proof_receipt` transaction hash were filled.

Wasm build verified in WSL:

```text
contract/wasm/ProofReceiptRegistry.wasm
sha256: 1a9add6be7dfc1dd2023c1c752fbc252890db22c0415adb137fd9e3c8a19bbcf
```

Status: public repo/demo/payload/Wasm/Testnet evidence ready; final DoraHacks submission still requires the submitter account and terms flow.
