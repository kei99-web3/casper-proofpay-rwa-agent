# Demo Video Script

Target: 75-90 seconds.

## 0-15s

Show Casper Testnet Explorer first.

Required shot for final submission:

- contract/package hash
- `record_proof_receipt` transaction/deploy hash
- visible success/executed status

Say:

> This is the Casper Testnet receipt produced by ProofPay. The rest of the demo shows the agent flow that generated this proof payload.

If the Testnet transaction is not complete yet, do not record the final version. Use the current draft video only as a temporary walkthrough.

## 15-25s

Show title:

> Casper ProofPay: AI agents buy verified revenue proofs before making financial decisions.

Say:

> This is a revenue proof market for Casper. A lending or risk agent pays for a proof, the proof agent validates revenue records, and Casper stores the receipt.

## 25-40s

Run:

```bash
npm test
npm run demo
```

Point to:

- 402 payment challenge
- mock payment proof
- deterministic proof root

## 40-55s

Open `demo/index.html`.

Show:

- revenue validation score
- proof root
- payment hash
- Casper transaction plan

## 55-70s

Show `contract/src/proof_receipt_registry.rs`.

Say:

> The transaction-producing component is `record_proof_receipt`, which records proof id, proof root, payment hash, receipt hash, quality score, and agent id on Casper Testnet.

## 70-85s

Show MCP tool output:

- `verify_revenue_proof`
- `get_agent_reputation`

Say:

> Other agents can verify the paid proof before making lending, underwriting, treasury, or risk decisions.

## 85-95s

Close:

> Synthetic data is used for the demo. Production adapters can connect accounting, payment, IoT, or attestation sources without putting raw private data on-chain.
