//! Odra contract build script.

/// Uses `ODRA_MODULE` to set the `odra_module` cfg flag.
pub fn main() {
    odra_build::build();
}
