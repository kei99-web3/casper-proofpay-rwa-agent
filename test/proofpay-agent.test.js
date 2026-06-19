"use strict";

const assert = require("assert");
const { createMcpTools } = require("../src/mcp-tools");
const { createSubmissionPayload } = require("../src/submission-payload");
const {
  DEFAULT_REVENUE_BATCH,
  runProofPayScenario,
  validateRevenueBatch
} = require("../src/proofpay-agent");

function testRevenueValidation() {
  const validation = validateRevenueBatch(DEFAULT_REVENUE_BATCH);
  assert.strictEqual(validation.totals.grossUsd, 7533.55);
  assert.strictEqual(validation.totals.txCount, 498);
  assert.strictEqual(validation.totals.averageTicketUsd, 15.13);
  assert.strictEqual(validation.verdict, "verified");
  assert.deepStrictEqual(validation.anomalies, []);
}

function testProofPayScenario() {
  const scenario = runProofPayScenario();
  assert.strictEqual(scenario.challenge.status, 402);
  assert.strictEqual(scenario.challenge.scheme, "x402-casper-mock");
  assert.strictEqual(scenario.receipt.domain, "synthetic_rwa_revenue");
  assert.strictEqual(scenario.receipt.validation.qualityScore, 96);
  assert.strictEqual(scenario.casperTransactionPlan.transactionProducing, true);
  assert.strictEqual(scenario.casperTransactionPlan.entryPoint, "record_proof_receipt");
}

function testMcpToolShape() {
  const scenario = runProofPayScenario();
  const mcp = createMcpTools({
    receipt: scenario.receipt,
    casperTransactionPlan: scenario.casperTransactionPlan
  });
  assert.strictEqual(mcp.tools.length, 2);
  assert.strictEqual(mcp.tools[0].name, "verify_revenue_proof");
  assert.strictEqual(mcp.tools[0].result.verified, true);
  assert.strictEqual(mcp.tools[1].result.reputation, "trusted_demo_agent");
}

function testDeterminism() {
  const first = runProofPayScenario();
  const second = runProofPayScenario();
  assert.strictEqual(first.receipt.proofRoot, second.receipt.proofRoot);
  assert.strictEqual(first.receipt.receiptHash, second.receipt.receiptHash);
  assert.strictEqual(first.casperTransactionPlan.args.proof_root, second.casperTransactionPlan.args.proof_root);
}

function testSubmissionPayload() {
  const scenario = runProofPayScenario();
  const payload = createSubmissionPayload();
  assert.strictEqual(payload.projectName, "Casper ProofPay: Revenue Proof Market for AI Agents");
  assert.strictEqual(payload.chainName, "casper-test");
  assert.strictEqual(payload.entryPoint, "record_proof_receipt");
  assert.deepStrictEqual(payload.proofReceiptArgs, scenario.casperTransactionPlan.args);
  assert.strictEqual(payload.localEvidence.receiptHash, scenario.receipt.receiptHash);
}

testRevenueValidation();
testProofPayScenario();
testMcpToolShape();
testDeterminism();
testSubmissionPayload();

console.log("proofpay-agent.test.js passed");
