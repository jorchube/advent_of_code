mod one;

fn main() {
    let one = one::solver::Solver::solve_base(include_str!("one/problem_input.txt"));
    println!("One: {}", one);

    let one_extra = one::solver::Solver::solve_extra(include_str!("one/problem_input.txt"));
    println!("One extra: {}", one_extra);
}
