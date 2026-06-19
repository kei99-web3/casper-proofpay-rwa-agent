# DoraHacks Submission Draft

## Project Name

Casper ProofPay: Revenue Proof Market for AI Agents

## Short Description

An agentic revenue proof market where AI lending, underwriting, treasury, and risk agents buy verified RWA revenue proofs before making financial decisions, verify receipts through MCP-style tools, and anchor proof receipts on Casper Testnet.

## Longer Description

Casper ProofPay turns synthetic real-world revenue records into paid, verifiable facts for other agents. A lending or risk agent receives an HTTP 402-style payment challenge, submits a payment proof, and receives a deterministic proof receipt before trusting a revenue stream. The receipt includes a proof root, payment hash, quality score, and agent id. The planned Casper Testnet contract records these receipt fields through a transaction-producing `record_proof_receipt` entry point.

MCP-style tools let downstream agents verify the proof and inspect the issuer reputation. The demo uses synthetic data only; production adapters can connect accounting, payment processor, IoT, TEE, or oracle attestations. The core use case is pre-decision revenue evidence for autonomous finance agents.

## Tech Stack

- Node.js deterministic proof engine
- x402-shaped payment challenge mock
- MCP-style verification tool schemas
- Odra-style Casper receipt registry scaffold
- Static HTML judge demo

## Repository

https://github.com/kei99-web3/casper-proofpay-rwa-agent

## Hosted Demo

https://kei99-web3.github.io/casper-proofpay-rwa-agent/

## Demo Video

Draft video URL:

https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-draft.mp4

Before final submission, replace or supplement this with a walkthrough that includes the Casper Testnet transaction hash.

## Casper Testnet Contract Address

To be filled after user-controlled Testnet deploy.

## Casper Testnet Transaction Hash

To be filled after one proof receipt transaction.
