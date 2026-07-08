# Contributing

Thanks for reviewing Casper ProofPay. This repository is a buildathon submission, so contributions should keep the project easy for judges and reviewers to run.

## Local checks

Run the main deterministic checks before opening a pull request:

```bash
npm test
npm run demo
npm run payload
npm run readiness
```

## Public safety boundary

Do not commit or paste:

- private keys, seed phrases, wallet files, or deploy keys
- `.env` files or API tokens
- customer data or real financial records
- private Casper account material

The included revenue data is synthetic. New examples should remain synthetic unless a future production adapter is reviewed separately.

## Casper evidence changes

If a change adds or changes Casper Testnet evidence, include:

- deploy hash
- package hash or contract hash when relevant
- explorer URL
- a short description of what the transaction proves

## Pull request shape

Keep pull requests small and focused. Include the command output summary from the local checks and explain any skipped verification.
