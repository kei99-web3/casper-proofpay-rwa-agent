"use strict";

const { runProofPayScenario } = require("./proofpay-agent");

function createSubmissionPayload() {
  const scenario = runProofPayScenario();
  return {
    projectName: "Casper ProofPay: Revenue Proof Market for AI Agents",
    network: "casper-testnet",
    chainName: "casper-test",
    contractName: scenario.casperTransactionPlan.contractName,
    entryPoint: scenario.casperTransactionPlan.entryPoint,
    transactionProducing: true,
    proofReceiptArgs: scenario.casperTransactionPlan.args,
    localEvidence: {
      proofId: scenario.receipt.proofId,
      proofRoot: scenario.receipt.proofRoot,
      paymentHash: scenario.receipt.paymentHash,
      receiptHash: scenario.receipt.receiptHash,
      qualityScore: scenario.receipt.validation.qualityScore,
      verdict: scenario.receipt.validation.verdict,
      issuedAt: scenario.receipt.issuedAt
    },
    publicArtifactsNeeded: [
      "Casper Testnet contract/package hash",
      "record_proof_receipt transaction/deploy hash",
      "Casper Testnet explorer URL",
      "Final demo video URL with Testnet evidence"
    ],
    safetyBoundary: "Do not commit private keys, wallet files, seed phrases, .env files, or live credentials."
  };
}

module.exports = { createSubmissionPayload };
