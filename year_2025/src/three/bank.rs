#[derive(Debug)]
pub struct Bank {
    batteries_raw: String,
    capacities: Vec<u32>,
}

impl Bank {
    pub fn new(batteries_raw: String) -> Self {
        let capacities = Bank::capacities(&batteries_raw);
        Bank {
            batteries_raw,
            capacities,
        }
    }

    pub fn get_biggest_joltage(&self) -> u32 {
        let mut capacities = self.capacities.clone();

        let tens_index = self.get_biggest_index(
            &capacities.as_slice()[0..capacities.len() - 1].to_vec(),
            None,
        );
        let tens = capacities[tens_index];
        let units_index = self.get_biggest_index(&capacities, Some(tens_index));
        let units = capacities[units_index];

        let joltage = tens * 10 + units;
        #[cfg(debug_assertions)]
        println!(
            "bank:{:?}, tens: {:?}, units: {:?}, joltage: {:?}",
            self.capacities, tens, units, joltage
        );

        joltage
    }

    fn get_biggest_index(&self, capacities: &Vec<u32>, skip_until: Option<usize>) -> usize {
        let mut biggest_index: Option<usize> = None;

        for index in 0..capacities.len() {
            if let Some(index_to_skip) = skip_until {
                if index_to_skip >= index {
                    continue;
                }
            }
            match biggest_index {
                None => biggest_index = Some(index),
                Some(current_biggest_index) => {
                    if capacities[index] > capacities[current_biggest_index] {
                        biggest_index = Some(index);
                    }
                }
            }
        }

        #[cfg(debug_assertions)]
        println!(
            "get biggest_index -> capacities {:?}, index: {:?}",
            capacities, biggest_index
        );

        biggest_index.unwrap()
    }

    fn capacities(batteries_raw: &String) -> Vec<u32> {
        batteries_raw
            .as_str()
            .chars()
            .filter_map(|c| c.to_digit(10))
            .collect()
    }
}
