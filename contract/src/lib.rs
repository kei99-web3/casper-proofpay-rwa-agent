#![cfg_attr(not(test), no_std)]
#![cfg_attr(not(test), no_main)]
extern crate alloc;

pub mod proof_receipt_registry;

pub use proof_receipt_registry::{ProofReceipt, ProofReceiptRegistry};
