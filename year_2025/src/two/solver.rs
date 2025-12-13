use crate::two::id::Id;

use super::id_ranges_parser::IdRangesParser;

pub struct Solver;

impl Solver {
    pub fn solve_base(input: &str) -> u64 {
        let ranges = IdRangesParser::parse(input.to_string());

        let ids = ranges
            .iter()
            .flat_map(|range| range.ids())
            .collect::<Vec<Id>>();
        let invalid_ids = ids.iter().filter(|id| !id.is_valid()).collect::<Vec<&Id>>();
        let ids_as_u64 = invalid_ids
            .iter()
            .map(|id| id.as_u64())
            .collect::<Vec<u64>>();
        let sum = ids_as_u64.iter().sum::<u64>();

        sum
    }

    pub fn solve_extra(input: &str) -> u64 {
        let ranges = IdRangesParser::parse(input.to_string());

        let ids = ranges
            .iter()
            .flat_map(|range| range.ids())
            .collect::<Vec<Id>>();
        let invalid_ids = ids
            .iter()
            .filter(|id| !id.is_valid_extra())
            .collect::<Vec<&Id>>();
        let ids_as_u64 = invalid_ids
            .iter()
            .map(|id| id.as_u64())
            .collect::<Vec<u64>>();
        let sum = ids_as_u64.iter().sum::<u64>();

        sum
    }
}
