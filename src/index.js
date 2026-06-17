"use strict";

const { runProofPayScenario } = require("./proofpay-agent");
const { createMcpTools } = require("./mcp-tools");

function main() {
  const scenario = runProofPayScenario();
  const mcp = createMcpTools({
    receipt: scenario.receipt,
    casperTransactionPlan: scenario.casperTransactionPlan
  });
  console.log(JSON.stringify({ ...scenario, mcp }, null, 2));
}

if (require.main === module) {
  main();
}

module.exports = { main };
