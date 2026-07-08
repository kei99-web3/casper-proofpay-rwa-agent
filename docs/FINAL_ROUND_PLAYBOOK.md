# Final Round Reviewer Playbook

This playbook is for Casper Agentic Buildathon reviewers who want the shortest path from repository to working evidence.

## 1. Open the live demo

Demo page:

https://kei99-web3.github.io/casper-proofpay-rwa-agent/

The demo walks through a buyer agent requesting a revenue proof, receiving an x402-style payment challenge, verifying a synthetic RWA revenue batch, and anchoring the proof receipt on Casper Testnet.

## 2. Watch the evidence-first demo video

Final demo video:

https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-final.mp4

The video begins with the Casper Testnet evidence before showing the product workflow.

## 3. Verify Casper Testnet evidence

Contract package hash:

```text
b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2
```

Contract hash:

```text
f56cf425f3a10ed7f3e9e2622b64ca2f2a0609c9446b1cb79ea2b58167293c61
```

Contract deploy hash:

```text
930222bfc49b84b775e9c5b008651432e7614025624df410aac993efcafd4d3d
```

Sample `record_proof_receipt` deploy:

```text
2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994
```

Explorer URL:

https://testnet.cspr.live/deploy/2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994

## 4. Run the local MVP

```bash
npm test
npm run demo
npm run payload
npm run readiness
```

What each command proves:

- `npm test`: deterministic proof flow and MCP-style verification behavior
- `npm run demo`: end-to-end mock agent workflow in the terminal
- `npm run payload`: exact deterministic argument set used for the Casper receipt
- `npm run readiness`: final submission fields are present

## 5. Inspect the contract package

The Odra contract source is in `contract/src/proof_receipt_registry.rs`.

The committed Wasm artifact is:

```text
contract/wasm/ProofReceiptRegistry.wasm
```

Expected sha256:

```text
1a9add6be7dfc1dd2023c1c752fbc252890db22c0415adb137fd9e3c8a19bbcf
```

## 6. Boundary notes

- The data is synthetic by design.
- No private key, seed phrase, wallet file, `.env`, API key, or customer data is committed.
- The x402 flow is modeled as a deterministic HTTP 402-style proof purchase, not a live payment facilitator.
- The Casper component is a real Testnet receipt registry deploy and sample receipt transaction.
