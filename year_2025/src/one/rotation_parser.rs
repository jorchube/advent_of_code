use super::rotation::Rotation;

pub struct RotationParser;

impl RotationParser {
    pub fn parse(data: String) -> Vec<super::rotation::Rotation> {
        let lines = data.trim().lines().collect::<Vec<&str>>();

        let rotations = lines
            .iter()
            .map(|line| Rotation::new(line))
            .collect::<Vec<Rotation>>();

        rotations
    }
}
