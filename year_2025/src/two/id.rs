use std::ops::Add;

#[derive(Debug, Clone)]
pub struct Id {
    value: String,
}

impl Id {
    pub fn new(value: String) -> Self {
        Id { value }
    }

    pub fn is_valid(&self) -> bool {
        let valid = self._is_valid();
        #[cfg(debug_assertions)]
        println!("{:?} {:?}", &self, valid);

        valid
    }

    pub fn is_valid_extra(&self) -> bool {
        let valid = self._is_valid_extra();
        #[cfg(debug_assertions)]
        println!("### {:?} {:?}", &self, valid);

        valid
    }

    pub fn as_u64(&self) -> u64 {
        self.value.parse::<u64>().unwrap()
    }

    fn _is_valid(&self) -> bool {
        if self.value.len() % 2 != 0 {
            return true;
        }

        let halves = self.value.split_at(self.value.len() / 2);
        if halves.0.eq(halves.1) {
            return false;
        }

        true
    }

    fn _is_valid_extra(&self) -> bool {
        let len = self.value.len();
        let divisors = self._divisors(len);
        #[cfg(debug_assertions)]
        println!("Divisors of {}: {:?}", len, &divisors);

        let is_valid = divisors
            .iter()
            .all(|divisor| self._is_valid_for_divisor(*divisor));

        is_valid
    }

    fn _is_valid_for_divisor(&self, divisor: usize) -> bool {
        let parts = self._split_into_parts(divisor);
        if parts.windows(2).all(|w| w[0] == w[1]) {
            return false;
        }

        true
    }

    fn _split_into_parts(&self, divisor: usize) -> Vec<&str> {
        let mut parts = Vec::new();
        let part_length = self.value.len() / divisor;
        for i in 0..divisor {
            let start = i * part_length;
            let end = start + part_length;
            parts.push(&self.value[start..end]);
        }
        #[cfg(debug_assertions)]
        println!(
            "Splitting {:?} with divisor {} into parts of length {}: {:?}",
            &self, divisor, part_length, parts
        );
        parts
    }

    fn _divisors(&self, value: usize) -> Vec<usize> {
        let mut divisors = Vec::new();
        let half = value.div_ceil(2);
        for i in 2..=half {
            if value % i == 0 {
                divisors.push(i);
            }
        }
        divisors.push(value);
        divisors
    }
}
