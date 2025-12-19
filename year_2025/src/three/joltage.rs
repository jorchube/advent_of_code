use std::iter::Sum;

use num_bigint::BigUint;

#[derive(Debug)]
pub struct Joltage {
    value: BigUint,
}

impl Joltage {
    pub fn new(value: BigUint) -> Self {
        Joltage { value }
    }

    pub fn from_batteries(tens: u32, units: u32) -> Self {
        let joltage_value = tens * 10 + units;
        Joltage {
            value: BigUint::from(joltage_value),
        }
    }

    pub fn value(&self) -> BigUint {
        self.value.clone()
    }
}

impl Sum for Joltage {
    fn sum<I: Iterator<Item = Joltage>>(iter: I) -> Self {
        let mut total = BigUint::from(0u32);

        for joltage in iter {
            total += joltage.value();
        }

        Joltage::new(total)
    }
}

impl ToString for Joltage {
    fn to_string(&self) -> String {
        self.value.to_string()
    }
}
