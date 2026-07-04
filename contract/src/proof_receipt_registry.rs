//! Odra-style Casper proof receipt registry.
//!
//! This is the intended transaction-producing on-chain component. It contains
//! no keys, accounts, deploy configuration, or live credentials.

use odra::prelude::*;
use odra::{Mapping, Var};

#[odra::module]
pub struct ProofReceiptRegistry {
    receipts: Mapping<String, ProofReceipt>,
    receipt_count: Var<u64>,
}

#[odra::odra_type]
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct ProofReceipt {
    pub proof_id: String,
    pub proof_root: String,
    pub payment_hash: String,
    pub receipt_hash: String,
    pub quality_score: u32,
    pub agent_id: String,
    pub recorded_by: Address,
}

#[odra::module]
impl ProofReceiptRegistry {
    pub fn init(&mut self) {
        self.receipt_count.set(0);
    }

    pub fn record_proof_receipt(
        &mut self,
        proof_id: String,
        proof_root: String,
        payment_hash: String,
        receipt_hash: String,
        quality_score: u32,
        agent_id: String,
    ) {
        assert!(quality_score <= 100, "quality_score must be 0..100");
        assert!(!proof_id.is_empty(), "proof_id required");
        assert!(!proof_root.is_empty(), "proof_root required");
        assert!(!payment_hash.is_empty(), "payment_hash required");
        assert!(!receipt_hash.is_empty(), "receipt_hash required");
        assert!(self.receipts.get(&proof_id).is_none(), "proof already recorded");

        let receipt = ProofReceipt {
            proof_id: proof_id.clone(),
            proof_root,
            payment_hash,
            receipt_hash,
            quality_score,
            agent_id,
            recorded_by: self.env().caller(),
        };

        self.receipts.set(&proof_id, receipt);
        self.receipt_count.set(self.receipt_count.get_or_default() + 1);
    }

    pub fn get_receipt(&self, proof_id: String) -> Option<ProofReceipt> {
        self.receipts.get(&proof_id)
    }

    pub fn total_receipts(&self) -> u64 {
        self.receipt_count.get_or_default()
    }
}
