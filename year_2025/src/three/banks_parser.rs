use super::bank::Bank;

pub struct BanksParser;

impl BanksParser {
    pub fn parse(input: String) -> Vec<Bank> {
        let lines: Vec<String> = input.trim().lines().map(|s| s.to_string()).collect();

        lines.iter().map(|line| Bank::new(line.clone())).collect()
    }
}
