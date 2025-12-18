#[derive(Debug)]
pub struct Bank {
    capacities: Vec<u32>,
}

impl Bank {
    pub fn new(batteries_raw: String) -> Self {
        Bank {
            capacities: Bank::capacities(&batteries_raw),
        }
    }

    pub fn get_biggest_joltage(&self) -> u32 {
        let tens_index = self.get_biggest_index_skipping_last(&self.capacities);
        let tens = self.capacities[tens_index];
        let units_index = self.get_biggest_index_skipping_until(&self.capacities, tens_index);
        let units = self.capacities[units_index];
        let joltage = tens * 10 + units;

        #[cfg(debug_assertions)]
        println!(
            "bank:{:?}, tens: {:?}, units: {:?}, joltage: {:?}",
            self.capacities, tens, units, joltage
        );

        joltage
    }

    fn get_biggest_index_skipping_last(&self, capacities: &Vec<u32>) -> usize {
        self.get_biggest_index(&capacities[0..capacities.len() - 1].to_vec(), None)
    }

    fn get_biggest_index_skipping_until(&self, capacities: &Vec<u32>, skip_until: usize) -> usize {
        self.get_biggest_index(capacities, Some(skip_until))
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
