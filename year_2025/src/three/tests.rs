#[cfg(test)]
mod tests {
    use crate::three::solver::Solver;

    #[test]
    fn example_input_base_problem() {
        let data = include_str!("example_input.txt");

        let result = Solver::solve_base(data);

        assert_eq!(result, "357");
    }

    #[test]
    fn example_input_extra_problem() {
        let data = include_str!("example_input.txt");

        let result = Solver::solve_extra(data);

        assert_eq!(result, "3121910778619");
    }
}
