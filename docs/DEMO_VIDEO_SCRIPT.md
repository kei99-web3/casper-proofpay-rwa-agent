# Demo Video Script

Status: final v2 rendered with licensed BGM and transition SFX.

Target: 105 seconds, 1920x1080, 30fps, audio-enhanced and mute-safe.

Final file:

- `media/casper-proofpay-demo-final.mp4`
- `media/casper-proofpay-demo-final-v2.mp4`

Build script:

```bash
python scripts/build-final-demo-video.py
```

Audio assets:

- BGM: Mixkit `Hazy After Hours` by Alejandro Magana (A. M.).
- Scene transition SFX: Mixkit `Message pop alert`.
- Credit and license notes: `media/audio/THIRD_PARTY_AUDIO.md`.

## Creative Strategy

Open with the underwriting question:

> Would you lend against this revenue stream?

Then show the proof path as a verification thread:

1. x402-shaped payment challenge.
2. synthetic RWA revenue validation.
3. tampered data rejection.
4. deterministic `record_proof_receipt` payload.
5. real Casper Testnet `record_proof_receipt` success.
6. MCP-style downstream verification.
7. public repo and hosted demo.

The video is intentionally not a slide deck. It uses actual local command output, public CSPR.live evidence, the hosted demo page, and the public GitHub repository.

The audio is intentionally subtle: the BGM gives the demo a polished bounty-video feel, while a short pop sound marks each major page/scene transition without covering the proof details.

## Scene Timeline

### 0:00-0:10 - Hook

On-screen:

```text
Would you lend against this revenue stream?
An AI agent just bought the proof.
qualityScore: 96
verdict: "verified"
Receipt recorded on Casper Testnet.
```

Purpose:

- Make the viewer care before showing architecture.
- Establish that the proof flow has both local output and Casper Testnet evidence.

### 0:10-0:22 - Thesis

On-screen:

```text
AI agents lend, underwrite, and allocate.
They should never act on unverified revenue.
ProofPay: agents BUY verified revenue proofs before they act.
```

Flow shown:

```text
Buyer Agent -> x402 Gate -> Proof Agent -> Casper Receipt -> MCP Verify
```

### 0:22-0:40 - Pay

Source: actual `npm run demo` output.

On-screen:

```text
STEP 1 / PAY - x402-shaped flow
"status": 402
"scheme": "x402-casper-mock"
"amount": "2.500000000" CSPR
paymentProof accepted
```

Boundary label:

```text
x402 mock - protocol-shaped, no real payment settled
```

### 0:40-1:00 - Verify

Source: actual `npm run demo` output plus local tamper check.

On-screen:

```text
STEP 2 / VERIFY - synthetic RWA revenue batch
grossUsd: 7533.55
txCount: 498
qualityScore: 96
verdict: "verified"
```

Then:

```text
tampered batch
needs_review
duplicate_source_day
non_positive_tx_count
```

Boundary label:

```text
synthetic demo data - no real customer revenue
```

### 1:00-1:18 - Anchor

Source: actual `npm run payload` output and public CSPR.live screenshot.

On-screen:

```text
STEP 3 / ANCHOR - Casper Testnet real transaction
"entryPoint": "record_proof_receipt"
"transactionProducing": true
"receipt_hash": "0a420465974a5784..."
Status: Success
record_proof_receipt
```

Evidence:

- Deploy hash: `2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994`
- Package hash: `b1ba96bf374ab52f3f6560a5e88ce4fe56324eb7846c5751f7f2c4ca90e499f2`
- Explorer URL: `https://testnet.cspr.live/deploy/2da236ad980f1a82943fe5485d36fdaa6c3c1cdd8b38dd42808aaaf1b25b3994`

Important honesty rule:

- The Explorer crop is used only for the real transaction, entry point, package hash, and success status.
- The video does not claim that the Explorer crop visibly displays the local `receipt_hash`.

### 1:18-1:32 - MCP

Source: actual `npm run demo` output.

On-screen:

```text
STEP 4 / RE-VERIFY - MCP-style tools
tool: "verify_revenue_proof"
result.verified: true
result.qualityScore: 96
tool: "get_agent_reputation"
reputation: "trusted_demo_agent"
```

Boundary label:

```text
MCP-style tool schema - local demo surface
```

### 1:32-1:45 - Close

Sources:

- Hosted demo screenshot.
- Public GitHub repository screenshot.

On-screen:

```text
Paid proof in. Verified receipt out. Anchored on Casper.
Public repo, README, usage instructions, and final video are public.
Run it yourself: npm test && npm run demo && npm run payload
```

Final safety line:

```text
Synthetic data demo. No private keys, no real funds.
x402 flow is protocol-shaped mock. Casper Testnet receipt is real.
```

## Acceptance Checks

- `ffprobe` confirms 105 seconds, 1920x1080, 30fps, H.264 video plus AAC audio.
- First 10 seconds include the underwriting question, local proof output, and Casper Testnet receipt mention.
- x402, synthetic data, and MCP are labeled honestly.
- Casper Testnet evidence shows `record_proof_receipt` and `Status: Success`.
- BGM and transition SFX are third-party Mixkit assets, not generated audio.
- The final URL remains stable for submission:
  `https://github.com/kei99-web3/casper-proofpay-rwa-agent/raw/main/media/casper-proofpay-demo-final.mp4`
