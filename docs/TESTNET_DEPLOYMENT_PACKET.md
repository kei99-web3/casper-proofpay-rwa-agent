# Testnet Deployment Packet

This project is ready for a user-controlled Casper Testnet proof step.

Codex/automation should not take custody of private keys, seed phrases, or wallet files. The submitter should run the wallet/faucet/signing steps in their own environment and paste only public artifacts back into the submission draft.

## Needed Public Artifacts

- Casper Testnet account hash or public key
- ProofReceiptRegistry contract package/hash or address
- One `record_proof_receipt` transaction/deploy hash
- Explorer link for the deploy/transaction

## Recommended Flow

1. Create or select a Casper Testnet account.
2. Request faucet funds.
3. Build/deploy `contract/proof_receipt_registry.rs` or an equivalent Odra/Casper contract.
4. Call `record_proof_receipt` with the local proof payload:

```json
{
  "proof_id": "proof-e9889ea33e5d",
  "proof_root": "e9889ea33e5dd20652c5e3b6b30aa44bd680f4caa399e089ba8f814b5e72ea2e",
  "payment_hash": "57410f7e0aca109956278cb80d5cf332b204ee3c942e6a62fcede8b055d85245",
  "receipt_hash": "0a420465974a5784c005ea47ead958d1ed3ed733ac2b2145c3d42e64224d5197",
  "quality_score": 96,
  "agent_id": "casper-proofpay-rwa-agent"
}
```

5. Update `docs/SUBMISSION_FORM_DRAFT.md` with the contract address/hash and transaction hash.
6. Record or update the demo video so it shows the Testnet proof.

## References

- Casper smart contract calling docs: https://docs.casper.network/developers/cli/calling-contracts
- Casper JavaScript/TypeScript SDK docs: https://docs.casper.network/developers/dapps/sdk/script-sdk
- Odra tutorials: https://developer.casper.network/odra-tutorials
- Casper AI Toolkit: https://www.casper.network/ai
