# Approval and Security

## Safe Local Actions

- Run `npm test`
- Run `npm run demo`
- Open `demo/index.html`
- Review `contract/proof_receipt_registry.rs`

## Not Included

This repository intentionally excludes:

- private keys
- wallet files
- seed phrases
- API keys
- `.env` files
- customer data
- real x402 settlement credentials
- Casper deploy artifacts containing account material

## External Actions Needed for Final Submission

The following actions require the submitter to use their own accounts and review each step:

1. Create or select a Casper Testnet account.
2. Request faucet funds.
3. Build and deploy the receipt registry contract.
4. Submit one `record_proof_receipt` transaction.
5. Capture contract address and transaction hash.
6. Publish a public demo video.
7. Submit the DoraHacks form.

The repository is designed so those actions can be performed without exposing raw revenue data or private keys in source control.

For a Japanese, non-engineer-friendly version of the remaining Testnet action, see `docs/USER_TESTNET_ACTION_GUIDE_JA.md`.
