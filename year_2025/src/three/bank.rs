use crate::three::joltage::Joltage;

#[derive(Debug)]
pub struct Bank {
    batteries: Vec<u32>,
}

impl Bank {
    pub fn new(batteries_raw: String) -> Self {
        Bank {
            batteries: Bank::batteries(&batteries_raw),
        }
    }

    pub fn get_biggest_joltage(&self) -> Joltage {
        let mut batteries: Vec<u32> = Vec::new();
        let batteries_length = self.batteries.len();

        let tens_index = self.get_biggest_battery_index_skipping_until_and_stopping_at(
            &self.batteries,
            None,
            batteries_length - 1,
        );
        let tens = self.batteries[tens_index];
        batteries.insert(0, tens);

        let units_index = self.get_biggest_battery_index_skipping_until_and_stopping_at(
            &self.batteries,
            Some(tens_index),
            batteries_length,
        );
        let units = self.batteries[units_index];
        batteries.insert(0, units);

        let joltage = Joltage::from_batteries(batteries);

        #[cfg(debug_assertions)]
        println!(
            "bank:{:?}, tens: {:?}, units: {:?}, joltage: {:?}",
            self.batteries, tens, units, joltage
        );

        joltage
    }

    fn get_biggest_battery_index_skipping_until_and_stopping_at(
        &self,
        batteries: &Vec<u32>,
        skip_until: Option<usize>,
        stop_at: usize,
    ) -> usize {
        self.get_biggest_index(&batteries[0..stop_at].to_vec(), skip_until)
    }

    fn get_biggest_index(&self, batteries: &Vec<u32>, skip_until: Option<usize>) -> usize {
        let mut biggest_index: Option<usize> = None;

        for index in 0..batteries.len() {
            if let Some(index_to_skip) = skip_until {
                if index_to_skip >= index {
                    continue;
                }
            }
            match biggest_index {
                None => biggest_index = Some(index),
                Some(current_biggest_index) => {
                    if batteries[index] > batteries[current_biggest_index] {
                        biggest_index = Some(index);
                    }
                }
            }
        }

        #[cfg(debug_assertions)]
        println!(
            "get biggest_index -> batteries {:?}, index: {:?}",
            batteries, biggest_index
        );

        biggest_index.unwrap()
    }

    fn batteries(batteries_raw: &String) -> Vec<u32> {
        batteries_raw
            .as_str()
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect()
    }
}
