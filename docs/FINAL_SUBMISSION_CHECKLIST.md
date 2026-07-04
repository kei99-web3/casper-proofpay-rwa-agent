# Final Submission Checklist

Use this checklist before pressing the DoraHacks submit button.

## Public Assets

- [x] Public GitHub repository exists.
- [x] Hosted demo exists.
- [x] Draft demo video exists.
- [x] README explains the revenue proof market narrative.
- [x] `npm test` passes.
- [x] `npm run payload` prints deterministic `record_proof_receipt` args.
- [x] `cargo odra build` produces `contract/wasm/ProofReceiptRegistry.wasm`.
- [ ] Final demo video includes real Casper Testnet evidence.

## Casper Testnet Evidence

- [x] Casper Testnet account was funded by faucet.
- [ ] `ProofReceiptRegistry` or equivalent receipt contract was deployed.
- [ ] Contract/package hash is recorded.
- [ ] `record_proof_receipt` or equivalent transaction was submitted.
- [ ] Transaction/deploy hash is recorded.
- [ ] Explorer URL opens publicly.
- [ ] README and `docs/SUBMISSION_FORM_DRAFT.md` include the Testnet evidence.

## DoraHacks Form

- [ ] Project name: `Casper ProofPay: Revenue Proof Market for AI Agents`.
- [ ] Repository URL: `https://github.com/kei99-web3/casper-proofpay-rwa-agent`.
- [ ] Hosted demo URL: `https://kei99-web3.github.io/casper-proofpay-rwa-agent/`.
- [ ] Demo video URL is final and public.
- [ ] Casper Testnet contract/package hash is included.
- [ ] `record_proof_receipt` transaction/deploy hash is included.
- [ ] Terms and eligibility are reviewed by the submitter.

## Do Not Submit If

- The Testnet transaction hash is missing.
- The explorer URL does not open publicly.
- The video only shows the local mock and no Testnet evidence.
- Any private key, wallet file, seed phrase, `.env`, API key, or customer data is present in the public repo.
