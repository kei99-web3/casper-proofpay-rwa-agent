"use strict";

const { createSubmissionPayload } = require("../src/submission-payload");

function main() {
  console.log(JSON.stringify(createSubmissionPayload(), null, 2));
}

if (require.main === module) {
  main();
}
