#[cfg(test)]
mod tests {
    use crate::one::dial::Dial;
    use crate::one::rotation::Rotation;

    #[test]
    fn example_input() {
        let data = include_str!("example_input.txt");
        let lines = data.trim().lines().collect::<Vec<&str>>();

        let rotations = lines
            .iter()
            .map(|line| Rotation::new(line))
            .collect::<Vec<Rotation>>();

        let mut dial = Dial::new(50);
        dial.rotate_multiple(rotations);

        assert_eq!(dial.zero_count(), 3);
    }
}
