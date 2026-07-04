"use strict";

const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");

const checks = [
  {
    id: "readme",
    label: "README explains the revenue proof market",
    ok: () => fs.readFileSync(path.join(root, "README.md"), "utf8").includes("Revenue Proof Market for AI Agents")
  },
  {
    id: "tests",
    label: "Local test file exists",
    ok: () => fs.existsSync(path.join(root, "test", "proofpay-agent.test.js"))
  },
  {
    id: "contract-scaffold",
    label: "Casper receipt registry scaffold exists",
    ok: () => fs.existsSync(path.join(root, "contract", "src", "proof_receipt_registry.rs"))
  },
  {
    id: "submission-payload",
    label: "Submission payload generator exists",
    ok: () => fs.existsSync(path.join(root, "scripts", "generate-submission-payload.js"))
  },
  {
    id: "testnet-contract",
    label: "Casper Testnet contract/package hash is filled",
    ok: () => !fs.readFileSync(path.join(root, "docs", "SUBMISSION_FORM_DRAFT.md"), "utf8").includes("To be filled after user-controlled Testnet deploy.")
  },
  {
    id: "testnet-transaction",
    label: "record_proof_receipt transaction hash is filled",
    ok: () => !fs.readFileSync(path.join(root, "docs", "SUBMISSION_FORM_DRAFT.md"), "utf8").includes("To be filled after one proof receipt transaction.")
  }
];

function main() {
  const results = checks.map((check) => ({ id: check.id, label: check.label, passed: Boolean(check.ok()) }));
  const missing = results.filter((result) => !result.passed);
  console.log(JSON.stringify({
    project: "casper-proofpay-rwa-agent",
    status: missing.length === 0 ? "ready_to_submit_after_user_approval" : "needs_more_evidence",
    results,
    nextRequiredPublicArtifacts: missing.map((result) => result.label)
  }, null, 2));
  process.exitCode = missing.length === 0 ? 0 : 1;
}

if (require.main === module) {
  main();
}
