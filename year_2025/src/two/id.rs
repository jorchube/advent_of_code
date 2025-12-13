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
}
