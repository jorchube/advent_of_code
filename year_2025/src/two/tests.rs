#[cfg(test)]
mod tests {
    use crate::two::solver::Solver;

    #[test]
    fn example_input_base_problem() {
        let data = include_str!("example_input.txt");

        let result = Solver::solve_base(data);

        assert_eq!(result, 1227775554);
    }

    #[test]
    fn example_input_extra_problem() {
        let data = include_str!("example_input.txt");

        let result = Solver::solve_extra(data);
        // let result = Solver::solve_extra("121211-121212");

        assert_eq!(result, 4174379265);
    }
}
