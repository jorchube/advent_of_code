use super::range::Range;

pub struct IdRangesParser;

impl IdRangesParser {
    pub fn parse(input: String) -> Vec<Range> {
        let line = input.lines().collect::<Vec<&str>>()[0];
        let raw_ranges = line.split(',').collect::<Vec<&str>>();

        let ranges = raw_ranges
            .iter()
            .map(|raw_range| {
                let bounds = raw_range
                    .split('-')
                    .map(|bound| bound.parse::<u32>().unwrap())
                    .collect::<Vec<u32>>();
                Range::new(bounds[0], bounds[1])
            })
            .collect::<Vec<Range>>();

        #[cfg(debug_assertions)]
        println!("{:?}", ranges);

        ranges
    }
}
