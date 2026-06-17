"use strict";

const { createMockPaymentProof, createX402Challenge, verifyMockPayment } = require("./x402-mock");
const { sha256, stableJson } = require("./utils");

const DEFAULT_REVENUE_BATCH = [
  { sourceId: "merchant-parking-a", day: "2026-06-10", grossUsd: 1842.25, txCount: 121 },
  { sourceId: "merchant-parking-a", day: "2026-06-11", grossUsd: 1904.1, txCount: 127 },
  { sourceId: "merchant-parking-a", day: "2026-06-12", grossUsd: 1775.4, txCount: 116 },
  { sourceId: "merchant-parking-a", day: "2026-06-13", grossUsd: 2011.8, txCount: 134 }
];

function validateRevenueBatch(batch) {
  const anomalies = [];
  const seen = new Set();
  const totals = batch.reduce((acc, row) => {
    const key = `${row.sourceId}:${row.day}`;
    if (seen.has(key)) anomalies.push({ key, reason: "duplicate_source_day" });
    seen.add(key);
    if (!row.sourceId || !row.day) anomalies.push({ key, reason: "missing_identity" });
    if (row.grossUsd <= 0) anomalies.push({ key, reason: "non_positive_gross" });
    if (row.txCount <= 0) anomalies.push({ key, reason: "non_positive_tx_count" });
    acc.grossUsd += row.grossUsd;
    acc.txCount += row.txCount;
    return acc;
  }, { grossUsd: 0, txCount: 0 });

  const grossUsd = Number(totals.grossUsd.toFixed(2));
  const averageTicketUsd = Number((grossUsd / totals.txCount).toFixed(2));
  const qualityScore = anomalies.length === 0 ? 96 : Math.max(50, 90 - anomalies.length * 12);

  return {
    totals: { grossUsd, txCount: totals.txCount, averageTicketUsd },
    anomalies,
    qualityScore,
    verdict: qualityScore >= 90 ? "verified" : "needs_review"
  };
}

function createProofReceipt({ batch, paymentProof }) {
  const validation = validateRevenueBatch(batch);
  const proofRoot = sha256(stableJson({ batch, validation }));
  const receipt = {
    proofId: `proof-${proofRoot.slice(0, 12)}`,
    domain: "synthetic_rwa_revenue",
    agentId: "casper-proofpay-rwa-agent",
    proofRoot,
    paymentHash: paymentProof.paymentHash,
    validation,
    issuedAt: "2026-06-17T12:00:05Z"
  };
  return { ...receipt, receiptHash: sha256(stableJson(receipt)) };
}

function createCasperTransactionPlan(receipt) {
  return {
    network: "casper-testnet",
    contractName: "ProofReceiptRegistry",
    entryPoint: "record_proof_receipt",
    transactionProducing: true,
    status: "ready_for_user_approved_testnet_deploy",
    args: {
      proof_id: receipt.proofId,
      proof_root: receipt.proofRoot,
      payment_hash: receipt.paymentHash,
      receipt_hash: receipt.receiptHash,
      quality_score: receipt.validation.qualityScore,
      agent_id: receipt.agentId
    }
  };
}

function runProofPayScenario({ batch = DEFAULT_REVENUE_BATCH } = {}) {
  const challenge = createX402Challenge({ proofId: "rwa-revenue-demo-001" });
  const paymentProof = createMockPaymentProof({ challenge });
  if (!verifyMockPayment({ challenge, paymentProof })) {
    throw new Error("Mock x402 payment proof failed verification");
  }
  const receipt = createProofReceipt({ batch, paymentProof });
  const casperTransactionPlan = createCasperTransactionPlan(receipt);
  return {
    title: "Casper ProofPay RWA Agent",
    summary: "Buy verified RWA revenue facts through x402, verify with MCP, anchor receipts on Casper.",
    challenge,
    paymentProof,
    receipt,
    casperTransactionPlan
  };
}

module.exports = {
  DEFAULT_REVENUE_BATCH,
  createCasperTransactionPlan,
  createProofReceipt,
  runProofPayScenario,
  sha256,
  stableJson,
  validateRevenueBatch
};
