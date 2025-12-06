use super::rotation::{Rotation, RotationDirection};

pub struct Dial {
    current_position: u32,
    zero_count: u32,
}

impl Dial {
    pub fn new(starting_point: u32) -> Self {
        Dial {
            current_position: starting_point,
            zero_count: 0,
        }
    }

    pub fn rotate(&mut self, rotation: Rotation) {
        let raw = rotation.raw_data();
        let clicks = rotation.clicks() % 100;
        let direction = rotation.direction();

        #[cfg(debug_assertions)]
        dbg!(
            "rotation: {raw} -> {direction:?}, {clicks}",
            raw,
            direction,
            clicks
        );

        let new_position;
        match direction {
            RotationDirection::Clockwise => {
                new_position = self.current_position + clicks;
            }
            RotationDirection::CounterClockwise => {
                new_position = self.current_position + 100 - (clicks);
            }
        }

        self.current_position = new_position % 100;
    }

    pub fn rotate_multiple(&mut self, rotations: Vec<Rotation>) {
        for rotation in rotations {
            self.rotate(rotation);
            if self.current_position == 0 {
                self.zero_count += 1;
            }
        }
    }

    pub fn zero_count(&self) -> u32 {
        self.zero_count
    }
}
