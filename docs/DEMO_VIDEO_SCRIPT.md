# Demo Video Script

Target: 75-90 seconds.

## 0-10s

Show title:

> Casper ProofPay RWA Agent: agents buy verified revenue facts, not raw spreadsheets.

Say:

> This is an agentic RWA proof service for Casper. A buyer agent pays for a proof, the proof agent validates revenue records, and Casper stores the receipt.

## 10-25s

Run:

```bash
npm test
npm run demo
```

Point to:

- 402 payment challenge
- mock payment proof
- deterministic proof root

## 25-45s

Open `demo/index.html`.

Show:

- revenue validation score
- proof root
- payment hash
- Casper transaction plan

## 45-65s

Show `contract/proof_receipt_registry.rs`.

Say:

> The transaction-producing component is `record_proof_receipt`, which records proof id, proof root, payment hash, receipt hash, quality score, and agent id on Casper Testnet.

## 65-80s

Show MCP tool output:

- `verify_revenue_proof`
- `get_agent_reputation`

Say:

> Other agents can verify the paid proof and decide whether to trust this revenue fact.

## 80-90s

Close:

> Synthetic data is used for the demo. Production adapters can connect accounting, payment, IoT, or attestation sources without putting raw private data on-chain.
