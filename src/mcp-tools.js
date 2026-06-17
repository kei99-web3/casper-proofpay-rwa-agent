"use strict";

function createMcpTools({ receipt, casperTransactionPlan }) {
  return {
    tools: [
      {
        name: "verify_revenue_proof",
        description: "Verify a paid RWA revenue proof receipt.",
        inputSchema: {
          type: "object",
          properties: {
            proof_id: { type: "string" },
            receipt_hash: { type: "string" }
          },
          required: ["proof_id", "receipt_hash"]
        },
        call: {
          proof_id: receipt.proofId,
          receipt_hash: receipt.receiptHash
        },
        result: {
          verified: true,
          verdict: receipt.validation.verdict,
          qualityScore: receipt.validation.qualityScore,
          grossUsd: receipt.validation.totals.grossUsd,
          txCount: receipt.validation.totals.txCount,
          anomalies: receipt.validation.anomalies,
          casperLookup: casperTransactionPlan.status
        }
      },
      {
        name: "get_agent_reputation",
        description: "Return the proof issuer's current local reputation model.",
        inputSchema: {
          type: "object",
          properties: {
            agent_id: { type: "string" }
          },
          required: ["agent_id"]
        },
        call: {
          agent_id: receipt.agentId
        },
        result: {
          agentId: receipt.agentId,
          proofsIssued: 1,
          latestQualityScore: receipt.validation.qualityScore,
          reputation: receipt.validation.qualityScore >= 90 ? "trusted_demo_agent" : "needs_more_history"
        }
      }
    ]
  };
}

module.exports = {
  createMcpTools
};
