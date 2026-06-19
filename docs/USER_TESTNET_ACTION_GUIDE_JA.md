# ユーザー向け Casper Testnet 対応ガイド

このファイルは、DoraHacks最終提出に必要な **Casper Testnet上で実際に動いた証拠** を取るためのガイドです。

## 重要な安全ルール

CodexやGitHub repoに以下を渡さないでください。

- 秘密鍵
- seed phrase
- wallet file
- `.env`
- API key
- OAuth/session cookie

Codexに渡してよいのは、公開情報だけです。

## あなたにお願いする公開情報

Testnet操作後、以下だけをCodexに渡してください。

```text
Casper Testnet account/public key:
Contract/package hash:
record_proof_receipt transaction/deploy hash:
Explorer URL for contract deploy:
Explorer URL for record_proof_receipt transaction:
DoraHacks追加質問やエラー:
```

## やること

1. Casper Testnet用のwallet/accountを用意する。
2. Testnet faucetでCSPRを取得する。
3. `ProofReceiptRegistry`相当のcontractをCasper Testnetへdeployする。
4. `npm run payload` の出力にある `proofReceiptArgs` を使って、`record_proof_receipt` を1回呼ぶ。
5. contract/package hash、transaction/deploy hash、explorer URLを保存する。
6. その公開情報だけをCodexへ渡す。

## payloadの取得

```bash
npm run payload
```

出力される `proofReceiptArgs` が、`record_proof_receipt` に入れる値です。

## readiness確認

```bash
npm run readiness
```

Testnet hash未入力の間は `needs_more_evidence` が出ます。これは正常です。

## 公式docs確認日

2026-06-19 JSTに以下を確認しました。

- Casper installing contracts docs: https://docs.casper.network/developers/cli/installing-contracts
- Casper calling contracts docs: https://docs.casper.network/developers/cli/calling-contracts
- Odra Casper backend docs: https://odra.dev/docs/backends/casper/
