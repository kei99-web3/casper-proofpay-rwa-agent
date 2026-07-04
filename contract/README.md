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

The canonical contract source is `src/proof_receipt_registry.rs`. The repository can be reviewed and built locally without a wallet.

Verified WSL build output:

```text
contract/wasm/ProofReceiptRegistry.wasm
sha256: 1a9add6be7dfc1dd2023c1c752fbc252890db22c0415adb137fd9e3c8a19bbcf
```

Casper Testnet deploy evidence:

1. Contract package hash: `b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2`
2. Contract hash: `f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61`
3. Contract deploy hash: `930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d`
4. `record_proof_receipt` deploy hash: `2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994`

## Build Skeleton

```text
contract/
  Cargo.toml
  Odra.toml
  Cargo.lock
  rust-toolchain
  bin/
    build_contract.rs
    build_schema.rs
  src/
    lib.rs
    proof_receipt_registry.rs
  wasm/
    ProofReceiptRegistry.wasm
```

Build command:

```bash
cd contract
cargo install cargo-odra
cargo odra build
```

Odra 2.8.x uses a pinned nightly toolchain. If `wasm-opt` fails on Ubuntu because the distro Binaryen is too old, install a newer Binaryen release and ensure `wasm-opt` is on `PATH`. If `wasm-strip` is missing, install WABT.

## Command Template

From the repository root:

```bash
npm run casper:commands
```

This prints a non-secret template for the install and `record_proof_receipt` call. Replace placeholders locally and never paste private key contents into chat, GitHub, or DoraHacks.
