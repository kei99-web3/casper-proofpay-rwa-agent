# Judging Requirements Map

Checked against the Casper Agentic Buildathon 2026 public brief on 2026-06-17.

| Requirement | This project |
| --- | --- |
| Agentic AI | Financial agents buy proof before acting; ProofPay issues paid proof receipts and exposes verification/reputation tools for downstream agents. |
| DeFi / RWA | Core RWA use case: verified synthetic revenue proofs for downstream lending, underwriting, treasury, or risk agents. |
| x402 | Pay-per-proof flow with a 402 challenge and payment proof hash. |
| MCP | `verify_revenue_proof` and `get_agent_reputation` MCP-style tool schemas. |
| Casper Testnet transaction-producing component | Verified `ProofReceiptRegistry.record_proof_receipt` transaction on Casper Testnet. |
| Open-source GitHub | This repository is a sanitized public candidate. |
| Demo video | Final MP4 in `media/casper-proofpay-demo-final.mp4`; public raw URL is listed in the submission draft. |

## Current Gaps Before Submission

- Deploy `ProofReceiptRegistry` on Casper Testnet. Done: `930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d`.
- Submit one transaction-producing receipt and capture the transaction hash. Done: `2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994`.
- Record a public demo video showing local proof flow plus Testnet receipt. Done: `media/casper-proofpay-demo-final.mp4`.
- Fill DoraHacks submission form with repo, video, contract address, and Testnet transaction hash.
