use super::banks_parser::BanksParser;

pub struct Solver;

impl Solver {
    pub fn solve_base(input: &str) -> u32 {
        let banks = BanksParser::parse(input.to_string());
        #[cfg(debug_assertions)]
        println!("{:?}", banks);

        let batteries: Vec<u32> = banks
            .iter()
            .map(|bank| bank.get_biggest_joltage())
            .collect();

        batteries.iter().sum()
    }

    pub fn solve_extra(input: &str) -> u32 {
        0
    }
}
