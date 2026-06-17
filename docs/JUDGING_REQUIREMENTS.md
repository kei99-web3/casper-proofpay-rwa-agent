# Judging Requirements Map

Checked against the Casper Agentic Buildathon 2026 public brief on 2026-06-17.

| Requirement | This project |
| --- | --- |
| Agentic AI | ProofPay issues paid proof receipts and exposes verification/reputation tools for other agents. |
| DeFi / RWA | Core RWA use case: verified synthetic revenue facts for downstream underwriting, treasury, or risk agents. |
| x402 | Pay-per-proof flow with a 402 challenge and payment proof hash. |
| MCP | `verify_revenue_proof` and `get_agent_reputation` MCP-style tool schemas. |
| Casper Testnet transaction-producing component | Planned `ProofReceiptRegistry.record_proof_receipt` transaction. |
| Open-source GitHub | This repository is a sanitized public candidate. |
| Demo video | Script in `docs/DEMO_VIDEO_SCRIPT.md`; public upload still required for final submission. |

## Current Gaps Before Submission

- Deploy `ProofReceiptRegistry` on Casper Testnet.
- Submit one transaction-producing receipt and capture the transaction hash.
- Record a public demo video showing local proof flow plus Testnet receipt.
- Fill DoraHacks submission form with repo, video, contract address, and Testnet transaction hash.
