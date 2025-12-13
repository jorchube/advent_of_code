mod one;
mod two;

fn main() {
    let one = one::solver::Solver::solve_base(include_str!("one/problem_input.txt"));
    println!("One: {}", one);

    let one_extra = one::solver::Solver::solve_extra(include_str!("one/problem_input.txt"));
    println!("One extra: {}", one_extra);

    let two = two::solver::Solver::solve_base(include_str!("two/problem_input.txt"));
    println!("Two: {}", two);
}
