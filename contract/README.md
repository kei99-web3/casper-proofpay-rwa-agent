# Casper Testnet Contract Plan

The on-chain component is a small proof receipt registry.

It is designed to satisfy the buildathon requirement for a transaction-producing Casper Testnet component:

```text
record_proof_receipt(proof_id, proof_root, payment_hash, receipt_hash, quality_score, agent_id)
```

## What Goes On-Chain

- `proof_id`: short identifier for the paid proof
- `proof_root`: deterministic hash of the validated revenue batch and validation result
- `payment_hash`: hash of the x402-shaped payment proof
- `receipt_hash`: hash of the issued proof receipt
- `quality_score`: validation score
- `agent_id`: issuing agent

## What Stays Off-Chain

- Raw revenue records
- Private customer data
- Wallet private keys
- x402 settlement credentials
- Production adapter credentials

## Current State

The canonical contract source is `src/proof_receipt_registry.rs`. The repository can be reviewed locally without a wallet. A real Casper Testnet deploy requires:

1. Casper Testnet account controlled by the submitter.
2. Faucet funds.
3. Rust/Casper/Odra build toolchain.
4. Signed deploy.
5. One `record_proof_receipt` transaction hash captured in the submission README and demo video.

## Build Skeleton

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
cargo odra build
```

The current Codex environment does not have `cargo` installed, so the Rust/Odra build must be verified in the submitter's local environment before Testnet deploy.

## Command Template

From the repository root:

```bash
npm run casper:commands
```

This prints a non-secret template for the install and `record_proof_receipt` call. Replace placeholders locally and never paste private key contents into chat, GitHub, or DoraHacks.
