# Casper ProofPay RWA Agent

Casper ProofPay RWA Agent is an agentic proof service for the Casper Agentic Buildathon 2026.

It lets an AI buyer agent purchase a verified real-world-asset revenue proof through an x402-shaped payment flow, verify the result through MCP-style tools, and anchor the proof receipt to a Casper Testnet contract.

Current status: local deterministic prototype and Casper Testnet receipt design. The repository contains no wallet, private key, faucet token, API key, customer data, or live transaction.

Public repository: https://github.com/kei99-web3/casper-proofpay-rwa-agent

Demo page: https://kei99-web3.github.io/casper-proofpay-rwa-agent/

Draft demo video: https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-draft.mp4

## Why This Fits Casper

The Casper Agentic Buildathon asks builders to create production-ready Agentic AI applications around Casper, especially DeFi and RWA, with a transaction-producing Casper Testnet component, open-source GitHub repository, and demo video.

This project targets that brief directly:

- **Agentic AI:** a proof agent validates revenue data, issues receipts, and exposes tools for other agents.
- **x402:** proof access is modeled as pay-per-request, using an HTTP 402-style challenge and payment proof.
- **MCP:** verification and reputation lookup are exposed as MCP-style tool responses.
- **RWA:** synthetic revenue facts stand in for future accounting, payment, IoT, or attestation adapters.
- **Casper Testnet:** the planned on-chain component records proof root, payment hash, receipt hash, quality score, and agent id.

## What the Demo Shows

1. A buyer agent asks for a revenue proof.
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
```

Open `demo/index.html` in a browser or use the GitHub Pages demo URL to view the judge-facing walkthrough.

The current MP4 is a short draft walkthrough. Before final DoraHacks submission, replace it or supplement it with a recorded Testnet transaction walkthrough after the Casper deploy is complete.

## Project Structure

```text
src/
  index.js                 CLI demo entrypoint
  proofpay-agent.js        Deterministic proof engine
  x402-mock.js             x402-shaped challenge/payment mock
  mcp-tools.js             MCP-style verification tool wrappers
contract/
  proof_receipt_registry.rs  Odra-style Casper contract scaffold
  README.md                  Testnet deployment plan
demo/
  index.html               Static judge demo
docs/
  JUDGING_REQUIREMENTS.md
  DEMO_VIDEO_SCRIPT.md
  APPROVAL_AND_SECURITY.md
  SUBMISSION_FORM_DRAFT.md
```

## Casper Testnet Component

The contract concept is a `ProofReceiptRegistry` with a transaction-producing entry point:

```text
record_proof_receipt(proof_id, proof_root, payment_hash, receipt_hash, quality_score, agent_id)
```

The local prototype produces the exact payload shape to pass into that entry point. A real Testnet deploy requires a Casper Testnet account, faucet funds, build toolchain, and a signed deploy. Those artifacts are intentionally excluded from this repository.

## Synthetic Data Boundary

The included revenue batch is synthetic. The goal is not to claim ownership of real assets. The goal is to prove the agentic architecture:

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

See `docs/APPROVAL_AND_SECURITY.md` for the publication and deploy boundary.
