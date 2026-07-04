"use strict";

const { createSubmissionPayload } = require("../src/submission-payload");
const WASM_PATH = "contract/wasm/ProofReceiptRegistry.wasm";

function q(value) {
  return `'${String(value).replace(/'/g, "'\"'\"'")}'`;
}

function main() {
  const payload = createSubmissionPayload();
  const args = payload.proofReceiptArgs;

  const installCommandQuickstart = [
    "casper-client put-deploy \\",
    "  --node-address https://node.testnet.cspr.cloud \\",
    "  --chain-name casper-test \\",
    "  --secret-key <LOCAL_SECRET_KEY_PATH_DO_NOT_SHARE> \\",
    "  --payment-amount <INSTALL_PAYMENT_AMOUNT_IN_MOTES> \\",
    `  --session-path ${WASM_PATH}`
  ].join("\n");

  const installCommandTransaction = [
    "casper-client put-transaction session \\",
    "  --node-address https://node.testnet.cspr.cloud \\",
    "  --chain-name casper-test \\",
    "  --secret-key <LOCAL_SECRET_KEY_PATH_DO_NOT_SHARE> \\",
    "  --gas-price-tolerance 10 \\",
    "  --pricing-mode fixed \\",
    `  --transaction-path ${WASM_PATH} \\`,
    "  --session-entry-point call \\",
    "  --category install-upgrade"
  ].join("\n");

  const callTemplate = [
    "casper-client put-deploy \\",
    "  --node-address https://node.testnet.cspr.cloud \\",
    "  --chain-name casper-test \\",
    "  --secret-key <LOCAL_SECRET_KEY_PATH_DO_NOT_SHARE> \\",
    "  --payment-amount <PAYMENT_AMOUNT_IN_MOTES> \\",
    "  --session-hash <CONTRACT_HASH_OR_PACKAGE_HASH> \\",
    "  --session-entry-point record_proof_receipt \\",
    `  --session-arg "proof_id:string=${q(args.proof_id)}" \\`,
    `  --session-arg "proof_root:string=${q(args.proof_root)}" \\`,
    `  --session-arg "payment_hash:string=${q(args.payment_hash)}" \\`,
    `  --session-arg "receipt_hash:string=${q(args.receipt_hash)}" \\`,
    `  --session-arg "quality_score:u32=${args.quality_score}" \\`,
    `  --session-arg "agent_id:string=${q(args.agent_id)}"`
  ].join("\n");

  console.log(JSON.stringify({
    warning: "Template only. Keep <LOCAL_SECRET_KEY_PATH_DO_NOT_SHARE> on your own machine and never paste key contents into chat, GitHub, or DoraHacks.",
    tools: [
      "cargo --version",
      "cargo install cargo-odra",
      "cargo install casper-client",
      "casper-client --version"
    ],
    build: [
      "cd contract",
      "cargo odra build",
      `ls wasm/ProofReceiptRegistry.wasm`
    ],
    wasmPath: WASM_PATH,
    installCommandQuickstart,
    installCommandTransaction,
    callTemplate,
    payload: payload.proofReceiptArgs,
    references: [
      "https://odra.dev/docs/basics/cargo-odra/",
      "https://docs.casper.network/developers/cli/installing-contracts",
      "https://docs.casper.network/developers/cli/calling-contracts"
    ]
  }, null, 2));
}

if (require.main === module) {
  main();
}
