use crate::three::joltage::Joltage;

use super::banks_parser::BanksParser;

pub struct Solver;

impl Solver {
    pub fn solve_base(input: &str) -> String {
        let banks = BanksParser::parse(input.to_string());
        #[cfg(debug_assertions)]
        println!("{:?}", banks);

        let joltages: Vec<Joltage> = banks
            .iter()
            .map(|bank| bank.get_biggest_joltage_for_n_batteries(2))
            .collect();

        let total: Joltage = joltages.into_iter().sum();

        total.to_string()
    }

    pub fn solve_extra(input: &str) -> String {
        let banks = BanksParser::parse(input.to_string());
        #[cfg(debug_assertions)]
        println!("{:?}", banks);

        let joltages: Vec<Joltage> = banks
            .iter()
            .map(|bank| bank.get_biggest_joltage_for_n_batteries(12))
            .collect();

        let total: Joltage = joltages.into_iter().sum();

        total.to_string()
    }
}
