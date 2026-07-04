# Testnet Deployment Packet

This project is prepared for a user-controlled Casper Testnet proof step. The local repository now includes an Odra project skeleton, but the final build, wallet, faucet, deploy, and transaction signing must happen in the submitter's own environment.

Codex/automation should not take custody of private keys, seed phrases, or wallet files. The submitter should run the wallet/faucet/signing steps in their own environment and paste only public artifacts back into the submission draft.

## Needed Public Artifacts

- Casper Testnet account hash or public key
- ProofReceiptRegistry contract package/hash or address
- One `record_proof_receipt` transaction/deploy hash
- Explorer link for the deploy/transaction

## Recommended Flow

1. Create or select a Casper Testnet account.
2. Request faucet funds.
3. Build/deploy the Odra contract project under `contract/`.
4. Verify local tools:

```bash
cargo --version
cargo install cargo-odra
cargo install casper-client
casper-client --version
```

5. Generate the local proof payload:

```bash
npm run payload
```

6. Generate a non-secret command template:

```bash
npm run casper:commands
```

This prints placeholder commands. Do not paste private keys or seed phrases anywhere.

7. Call `record_proof_receipt` with the generated `proofReceiptArgs`:

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

8. Update `docs/SUBMISSION_FORM_DRAFT.md` with the contract address/hash and transaction hash.
9. Record or update the demo video so it shows the Testnet proof.
10. Run `npm run readiness`; it should move from `needs_more_evidence` to `ready_to_submit_after_user_approval` after the Testnet fields are filled.

## Local Build Shape

The Odra docs currently describe `cargo odra build` as the build command that generates wasm files into a `wasm` folder. The minimal contract project has this shape:

```text
contract/
  Cargo.toml
  Odra.toml
  src/
    lib.rs
    proof_receipt_registry.rs
```

Build command:

```bash
cd contract
cargo install cargo-odra
cargo install casper-client
cargo odra build
```

Codex could not verify this locally because Rust/Cargo is not installed in the AI_Workspace execution environment. Verify it on the machine that will run the user-controlled deploy.

## Casper CLI Shape

The exact command depends on the final build toolchain and chosen node URL. The official Casper docs currently describe:

- Quickstart-style install with compiled Wasm, Casper CLI client, Casper account key pair, faucet-funded Testnet account, and `casper-client put-deploy --session-path`.
- Casper 2.0 Installing Contracts docs also show `casper-client put-transaction session` with `--transaction-path`, fixed pricing, and `install-upgrade`.
- Calling a stored contract by hash/package/name uses `put-deploy` with an entry point and optional session arguments.

`npm run casper:commands` prints both install shapes as non-secret templates. If one command is rejected by the installed client version, use the other official shape and share the exact error text.

Do not paste a real secret key path, private key, seed phrase, or wallet file into GitHub issues, chat, README, or DoraHacks text fields.

## References

- Casper smart contract calling docs: https://docs.casper.network/developers/cli/calling-contracts
- Casper installing contracts docs: https://docs.casper.network/developers/cli/installing-contracts
- Casper JavaScript/TypeScript SDK docs: https://docs.casper.network/developers/dapps/sdk/script-sdk
- Odra tutorials: https://developer.casper.network/odra-tutorials
- Odra Casper backend docs: https://odra.dev/docs/backends/casper/
- Casper AI Toolkit: https://www.casper.network/ai
