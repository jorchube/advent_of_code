#[cfg(test)]
mod tests {
    use crate::one::solver::Solver;

    #[test]
    fn example_input() {
        let data = include_str!("example_input.txt");

        let result = Solver::solve(data);

        assert_eq!(result, 3);
    }
}
