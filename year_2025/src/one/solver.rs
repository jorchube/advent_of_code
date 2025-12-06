pub struct Solver;

impl Solver {
    pub fn solve(input: &str) -> u32 {
        let rotations = super::rotation_parser::RotationParser::parse(input.to_string());
        let mut dial = super::dial::Dial::new(50);
        dial.rotate_multiple(rotations);

        dial.zero_count()
    }
}
