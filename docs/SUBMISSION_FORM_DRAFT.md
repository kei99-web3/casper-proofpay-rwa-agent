# DoraHacks Submission Draft

## Project Name

Casper ProofPay: Revenue Proof Market for AI Agents

## Short Description

An agentic revenue proof market where AI lending, underwriting, treasury, and risk agents buy verified RWA revenue proofs before making financial decisions, verify receipts through MCP-style tools, and anchor proof receipts on Casper Testnet.

## Longer Description

Casper ProofPay turns synthetic real-world revenue records into paid, verifiable facts for other agents. A lending or risk agent receives an HTTP 402-style payment challenge, submits a payment proof, and receives a deterministic proof receipt before trusting a revenue stream. The receipt includes a proof root, payment hash, quality score, and agent id. The Casper Testnet contract records these receipt fields through a transaction-producing `record_proof_receipt` entry point.

MCP-style tools let downstream agents verify the proof and inspect the issuer reputation. The demo uses synthetic data only; production adapters can connect accounting, payment processor, IoT, TEE, or oracle attestations. The core use case is pre-decision revenue evidence for autonomous finance agents.

## Tech Stack

- Node.js deterministic proof engine
- x402-shaped payment challenge mock
- MCP-style verification tool schemas
- Buildable Odra Casper receipt registry
- Static HTML judge demo

## Repository

https://github.com/kei99-web3/casper-proofpay-rwa-agent

## Hosted Demo

https://kei99-web3.github.io/casper-proofpay-rwa-agent/

## Demo Video

Final video URL:

https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-final.mp4

## Casper Testnet Contract Address

Contract package hash:

`b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2`

Contract hash:

`f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61`

Contract package explorer:

https://testnet.cspr.live/contract-package/b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2

Contract explorer:

https://testnet.cspr.live/contract/f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61

Contract deploy hash:

`930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d`

Contract deploy explorer:

https://testnet.cspr.live/deploy/930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d

## Casper Testnet Transaction Hash

`record_proof_receipt` deploy hash:

`2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994`

Explorer:

https://testnet.cspr.live/deploy/2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994
