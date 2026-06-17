"use strict";

const { sha256, stableJson } = require("./utils");

function createX402Challenge({ proofId, amount = "2.500000000", network = "casper-testnet" }) {
  const challenge = {
    status: 402,
    scheme: "x402-casper-mock",
    network,
    proofId,
    amount,
    asset: "CSPR",
    paymentAddress: "casper-testnet-payee-placeholder",
    payTo: "ProofPayRevenueProofService",
    expiresAt: "2026-06-30T00:00:00Z"
  };
  return { ...challenge, challengeHash: sha256(stableJson(challenge)) };
}

function createMockPaymentProof({ challenge, payerAgent = "buyer-agent-demo" }) {
  const paymentProof = {
    challengeHash: challenge.challengeHash,
    payerAgent,
    authorization: "mock_authorization_no_private_key_used",
    paidAt: "2026-06-17T12:00:00Z"
  };
  return { ...paymentProof, paymentHash: sha256(stableJson(paymentProof)) };
}

function verifyMockPayment({ challenge, paymentProof }) {
  return Boolean(
    challenge &&
    paymentProof &&
    challenge.challengeHash === paymentProof.challengeHash &&
    paymentProof.paymentHash === sha256(stableJson({
      challengeHash: paymentProof.challengeHash,
      payerAgent: paymentProof.payerAgent,
      authorization: paymentProof.authorization,
      paidAt: paymentProof.paidAt
    }))
  );
}

module.exports = {
  createMockPaymentProof,
  createX402Challenge,
  verifyMockPayment
};
