# Casper ProofPay: Revenue Proof Market for AI Agents

[![CI](https://github.com/kei99-web3/casper-proofpay-rwa-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kei99-web3/casper-proofpay-rwa-agent/actions/workflows/ci.yml)
[![CodeQL](https://github.com/kei99-web3/casper-proofpay-rwa-agent/actions/workflows/codeql.yml/badge.svg)](https://github.com/kei99-web3/casper-proofpay-rwa-agent/actions/workflows/codeql.yml)

Casper ProofPay is an agentic revenue proof market for the Casper Agentic Buildathon 2026.

It lets AI lending, underwriting, treasury, and risk agents buy verified real-world-asset revenue proofs before making financial decisions. Each proof is purchased through an x402-shaped payment flow, verified through MCP-style tools, and anchored as a receipt on Casper Testnet.

Current status: local deterministic prototype plus verified Casper Testnet receipt evidence. The repository contains no wallet, private key, faucet token, API key, or customer data.

Build status: the Odra contract builds locally to `contract/wasm/ProofReceiptRegistry.wasm`. The checked WSL build output sha256 is `1a9add6be7dfc1dd2023c1c752fbc252890db22c0415adb137fd9e3c8a19bbcf`.

Casper Testnet evidence:

- Contract package hash: `b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2`
- Contract hash: `f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61`
- Contract deploy hash: `930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d`
- `record_proof_receipt` deploy hash: `2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994`
- Explorer: https://testnet.cspr.live/deploy/2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994

Public repository: https://github.com/kei99-web3/casper-proofpay-rwa-agent

Demo page: https://kei99-web3.github.io/casper-proofpay-rwa-agent/

Final demo video: https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-final.mp4

Audio credits for the final demo video are documented in `media/audio/THIRD_PARTY_AUDIO.md`.

## Final Round Review Quick Links

- Reviewer playbook: [`docs/FINAL_ROUND_PLAYBOOK.md`](docs/FINAL_ROUND_PLAYBOOK.md)
- Live demo: https://kei99-web3.github.io/casper-proofpay-rwa-agent/
- Final demo video: https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-final.mp4
- Casper Testnet receipt deploy: https://testnet.cspr.live/deploy/2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994
- Contract package hash: `b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2`
- Security policy: [`SECURITY.md`](SECURITY.md)
- Contribution and public-boundary notes: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Why This Fits Casper

The Casper Agentic Buildathon asks builders to create production-ready Agentic AI applications around Casper, especially DeFi and RWA, with a transaction-producing Casper Testnet component, open-source GitHub repository, and demo video.

This project targets that brief directly:

- **Agentic AI:** financial agents buy proof before they act, while a proof agent validates revenue data, issues receipts, and exposes tools for downstream agents.
- **x402:** proof access is modeled as pay-per-request, using an HTTP 402-style challenge and payment proof.
- **MCP:** verification and reputation lookup are exposed as MCP-style tool responses.
- **RWA:** synthetic revenue proofs stand in for future accounting, payment, IoT, or attestation adapters.
- **Casper Testnet:** the on-chain component records proof root, payment hash, receipt hash, quality score, and agent id.

## What the Demo Shows

1. A lending or risk agent asks for a revenue proof before trusting a revenue stream.
2. The proof service returns a 402 payment challenge.
3. The buyer submits a mock x402 payment proof.
4. The RWA Proof Agent validates a synthetic revenue batch.
5. The agent returns a deterministic proof root and receipt hash.
6. The transaction plan shows the Casper Testnet `record_proof_receipt` call.
7. MCP-style verification tools return proof status and agent reputation.

## Quick Start

```bash
npm test
npm run demo
npm run payload
```

Open `demo/index.html` in a browser or use the GitHub Pages demo URL to view the judge-facing walkthrough.

`npm run payload` prints the exact deterministic `record_proof_receipt` argument set used for the Casper Testnet receipt transaction. `npm run readiness` checks that the final submission fields are filled.

## Project Structure

```text
src/
  index.js                 CLI demo entrypoint
  proofpay-agent.js        Deterministic proof engine
  x402-mock.js             x402-shaped challenge/payment mock
  mcp-tools.js             MCP-style verification tool wrappers
  submission-payload.js    Deterministic Testnet receipt args
scripts/
  generate-submission-payload.js
  check-readiness.js
  print-casper-client-template.js
contract/
  Cargo.toml                  Minimal Odra contract manifest
  Odra.toml                   ProofReceiptRegistry build target
  Cargo.lock                  Reproducible Rust dependency lockfile
  rust-toolchain              Nightly toolchain pin for Odra 2.8.x
  bin/                        Odra build/schema binaries
  src/proof_receipt_registry.rs
  wasm/ProofReceiptRegistry.wasm
  README.md                  Testnet deployment plan
demo/
  index.html               Static judge demo
docs/
  FINAL_ROUND_PLAYBOOK.md
  JUDGING_REQUIREMENTS.md
  DEMO_VIDEO_SCRIPT.md
  APPROVAL_AND_SECURITY.md
  SUBMISSION_FORM_DRAFT.md
  USER_TESTNET_ACTION_GUIDE_JA.md
  FINAL_SUBMISSION_CHECKLIST.md
```

## Casper Testnet Component

The contract concept is a `ProofReceiptRegistry` with a transaction-producing entry point:

```text
record_proof_receipt(proof_id, proof_root, payment_hash, receipt_hash, quality_score, agent_id)
```

The local prototype produces the exact payload shape passed into that entry point. The Testnet deploy and receipt transaction were signed from a separate funded Testnet key environment; private key material is intentionally excluded from this repository.

## Synthetic Data Boundary

The included revenue batch is synthetic. The goal is not to claim ownership of real assets. The goal is to prove the agentic market architecture:

- paid proof request
- deterministic validation
- signed receipt
- on-chain receipt registry
- MCP verification for downstream agents

In production, the `revenueBatch` adapter can be replaced with accounting exports, payment processor records, IoT telemetry, TEE attestations, or oracle attestations.

## Security Boundary

This repository does not contain:

- private keys
- wallet files
- API keys
- customer data
- `.env` files
- live x402 facilitator credentials
- Casper Testnet deploy secrets

See `docs/APPROVAL_AND_SECURITY.md` for the publication and deploy boundary, and `docs/TESTNET_DEPLOYMENT_PACKET.md` for the user-controlled Casper Testnet proof step.
