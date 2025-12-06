#[derive(Debug, Copy, Clone)]
pub enum RotationDirection {
    Clockwise,
    CounterClockwise,
}

pub struct Rotation {
    direction: RotationDirection,
    clicks: u32,
}

impl Rotation {
    pub fn new(raw_data: &str) -> Self {
        #[cfg(debug_assertions)]
        dbg!(raw_data);

        let (part0, part1) = raw_data.split_at(1);
        let direction = match part0 {
            "R" => RotationDirection::Clockwise,
            "L" => RotationDirection::CounterClockwise,
            _ => panic!("Invalid rotation direction"),
        };
        let clicks = part1.parse::<u32>().expect("Invalid number of clicks");

        #[cfg(debug_assertions)]
        dbg!(direction, clicks);

        Rotation { direction, clicks }
    }

    pub fn clicks(&self) -> u32 {
        self.clicks
    }

    pub fn direction(&self) -> &RotationDirection {
        &self.direction
    }
}
