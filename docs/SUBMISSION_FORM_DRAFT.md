# DoraHacks Submission Draft

## Project Name

Casper ProofPay RWA Agent

## Short Description

An agentic RWA proof service where AI agents buy verified revenue facts through an x402-shaped payment flow, verify receipts through MCP-style tools, and anchor proof receipts on Casper Testnet.

## Longer Description

Casper ProofPay RWA Agent turns synthetic real-world revenue records into paid, verifiable facts for other agents. A buyer agent receives an HTTP 402-style payment challenge, submits a payment proof, and receives a deterministic proof receipt. The receipt includes a proof root, payment hash, quality score, and agent id. The planned Casper Testnet contract records these receipt fields through a transaction-producing `record_proof_receipt` entry point.

MCP-style tools let downstream agents verify the proof and inspect the issuer reputation. The demo uses synthetic data only; production adapters can connect accounting, payment processor, IoT, TEE, or oracle attestations.

## Tech Stack

- Node.js deterministic proof engine
- x402-shaped payment challenge mock
- MCP-style verification tool schemas
- Odra-style Casper receipt registry scaffold
- Static HTML judge demo

## Repository

To be filled after public repo creation.

## Demo Video

To be filled after public video upload.

## Casper Testnet Contract Address

To be filled after user-controlled Testnet deploy.

## Casper Testnet Transaction Hash

To be filled after one proof receipt transaction.
