mod one;

fn main() {
    let one = one::solver::Solver::solve(include_str!("one/problem_input.txt"));
    println!("One: {}", one);
}
