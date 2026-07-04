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

## 全体像

今回の目的は、Casper Testnet上で以下の2つの公開証拠を取ることです。

1. `ProofReceiptRegistry` 相当のcontract deploy証拠
2. `record_proof_receipt` 相当のtransaction/deploy証拠

この2つがないと、DoraHacks提出要件の「transaction-producing on-chain component」を強く示せません。

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

## 0-10 手順

### 0. ゴールを確認する

最終的に、上のテンプレートを埋められればOKです。秘密情報は一切不要です。

### 1. 必要ページを開く

- Public repo: https://github.com/kei99-web3/casper-proofpay-rwa-agent
- Hosted demo: https://kei99-web3.github.io/casper-proofpay-rwa-agent/
- Casper docs: https://docs.casper.network/
- DoraHacks Casper page: https://dorahacks.io/hackathon/casper-agentic-buildathon/detail

### 2. Testnet用Wallet/accountを用意する

Casper WalletまたはCasper Testnet用accountを用意します。本番資産を持つwalletではなく、できればTestnet専用accountを使ってください。

seed phrase、private key、wallet fileはCodexにもGitHubにも貼らないでください。

### 3. Testnet public keyをコピーする

Wallet上でTestnetを選び、public keyまたはaccount hashをコピーします。これは公開情報なのでCodexに共有して構いません。

### 4. FaucetでTestnet CSPRを受け取る

Casper Testnet faucetで、Step 3の公開アドレスへTestnet CSPRを送ります。失敗した場合はエラー文だけ共有してください。

### 5. Repoをcloneしてpayloadを作る

```bash
git clone https://github.com/kei99-web3/casper-proofpay-rwa-agent.git
cd casper-proofpay-rwa-agent
npm test
npm run payload
```

`npm run payload` の出力が、`record_proof_receipt` に入れる証明データです。

### 6. ContractをTestnetにdeployする

`contract/` の `ProofReceiptRegistry` 相当の設計を使ってCasper Testnetへdeployします。ここは署名が必要になるため、あなたの環境で実行してください。

まず、公開repo内で非secretのテンプレートを確認します。

```bash
npm run casper:commands
```

Casper公式docsには、installについて `put-deploy --session-path` 型と `put-transaction session --transaction-path` 型の両方が出ています。このscriptは両方の非secretテンプレートを出します。あなたのPCに入った `casper-client` で片方が通らない場合は、秘密鍵の中身ではなくエラー全文だけCodexへ送ってください。

次に、Rust/Cargo/Odraが使える環境でWasmを作ります。

```bash
cd contract
cargo install cargo-odra
cargo install casper-client
cargo odra build
```

このCodex環境ではRust/Cargoが入っていなかったため、上記ビルドはあなたのPC側で確認してください。

### 7. Contract deploy hashを保存する

deploy後、contract/package hash、deploy hash、Explorer URLを保存します。

### 8. `record_proof_receipt` を1回呼ぶ

Step 5のpayloadを使い、`record_proof_receipt` 相当のentry pointを1回呼びます。

### 9. transaction hashを保存する

`record_proof_receipt` のtransaction/deploy hashとExplorer URLを保存します。

### 10. 公開情報だけCodexへ渡す

テンプレートを埋めてCodexへ渡してください。CodexはREADME、submission draft、demo scriptを更新します。

## 短縮版

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

2026-07-04 JSTに以下を再確認しました。

- Casper quickstart docs: https://docs.casper.network/resources/quick-start
- Casper installing contracts docs: https://docs.casper.network/developers/cli/installing-contracts
- Casper calling contracts docs: https://docs.casper.network/developers/cli/calling-contracts
- Odra Casper backend docs: https://odra.dev/docs/backends/casper/
