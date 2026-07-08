# Security Policy

## Supported scope

This repository is a Casper Agentic Buildathon proof-of-concept. Security review covers:

- deterministic proof engine behavior
- mock x402 payment challenge flow
- MCP-style verification tool outputs
- Casper Testnet receipt evidence and documentation
- public demo and submission files

The repository intentionally does not include private keys, wallet files, `.env` files, live x402 facilitator credentials, customer data, or production financial records.

## Reporting a vulnerability

Please open a GitHub security advisory or a private report through GitHub's security reporting flow for this repository.

Include:

- affected file or component
- reproduction steps
- expected impact
- whether the issue affects the mock demo, the Casper Testnet evidence, or only documentation

Do not include private keys, seed phrases, wallet files, access tokens, or real customer data in any report.

## Dependency and code scanning

This repository uses:

- Dependabot dependency updates for npm, Cargo, and GitHub Actions
- CodeQL for JavaScript and Python security analysis
- CI checks for deterministic tests, submission readiness, Wasm checksum, and public-boundary scans
