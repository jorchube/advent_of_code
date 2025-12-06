#[derive(Debug)]
pub enum RotationDirection {
    Clockwise,
    CounterClockwise,
}

pub struct Rotation {
    raw_data: String,
    direction: RotationDirection,
    clicks: u32,
}

impl Rotation {
    pub fn new(raw_data: &str) -> Self {
        println!("Parsing rotation from raw data: {}", raw_data);

        let (part0, part1) = raw_data.split_at(1);
        let direction = match part0 {
            "R" => RotationDirection::Clockwise,
            "L" => RotationDirection::CounterClockwise,
            _ => panic!("Invalid rotation direction"),
        };
        let clicks = part1.parse::<u32>().expect("Invalid number of clicks");

        Rotation {
            raw_data: raw_data.to_string(),
            direction,
            clicks,
        }
    }

    pub fn raw_data(&self) -> &str {
        &self.raw_data
    }

    pub fn clicks(&self) -> u32 {
        self.clicks
    }

    pub fn direction(&self) -> &RotationDirection {
        &self.direction
    }
}
