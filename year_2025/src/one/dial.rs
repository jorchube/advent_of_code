use super::rotation::{Rotation, RotationDirection};

pub struct Dial {
    current_position: u32,
    zero_count: u32,
    zero_passes: u32,
}

impl Dial {
    pub fn new(starting_point: u32) -> Self {
        Dial {
            current_position: starting_point,
            zero_count: 0,
            zero_passes: 0,
        }
    }

    pub fn rotate(&mut self, rotation: Rotation) {
        let clicks = rotation.clicks() % 100;
        let direction = rotation.direction();

        #[cfg(debug_assertions)]
        dbg!(direction, clicks);

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

    pub fn rotate_multiple_and_count_zero_passes(&mut self, rotations: Vec<Rotation>) {
        for rotation in rotations {
            let passes = self.count_zero_passes_brute(&rotation);
            self.rotate(rotation);
            self.zero_passes += passes;
        }
    }

    pub fn count_zero_passes(&mut self, rotation: &Rotation) -> u32 {
        let clicks = rotation.clicks();
        let direction = rotation.direction();

        let mut passes = clicks / 100;
        let remainder = clicks % 100;

        match direction {
            RotationDirection::Clockwise => {
                if remainder + self.current_position >= 100 {
                    passes += 1;
                }
            }
            RotationDirection::CounterClockwise => {
                if self.current_position < remainder {
                    passes += 1;
                }
            }
        }

        passes
    }

    pub fn count_zero_passes_brute(&mut self, rotation: &Rotation) -> u32 {
        let clicks = rotation.clicks();
        let direction = rotation.direction();

        let mut passes = 0;
        let mut position: i32 = self.current_position.try_into().unwrap();

        match direction {
            RotationDirection::Clockwise => {
                for _ in 0..clicks {
                    position = position + 1;
                    if position == 100 {
                        position = 0;
                        passes += 1;
                    }
                }
            }
            RotationDirection::CounterClockwise => {
                for _ in 0..clicks {
                    position = position - 1;
                    if position == 0 {
                        passes += 1;
                    }
                    if position == -1 {
                        position = 99;
                    }
                }
            }
        }

        passes
    }

    pub fn zero_count(&self) -> u32 {
        self.zero_count
    }

    pub fn zero_passes_count(&self) -> u32 {
        self.zero_passes
    }
}
