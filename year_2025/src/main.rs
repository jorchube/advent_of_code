mod one;
mod three;
mod two;

fn main() {
    let one = one::solver::Solver::solve_base(include_str!("one/problem_input.txt"));
    println!("One: {}", one);

    let one_extra = one::solver::Solver::solve_extra(include_str!("one/problem_input.txt"));
    println!("One extra: {}", one_extra);

    let two = two::solver::Solver::solve_base(include_str!("two/problem_input.txt"));
    println!("Two: {}", two);

    let two_extra = two::solver::Solver::solve_extra(include_str!("two/problem_input.txt"));
    println!("Two extra: {}", two_extra);

    let three = three::solver::Solver::solve_base(include_str!("three/problem_input.txt"));
    println!("Three: {}", three);

    let three_extra = three::solver::Solver::solve_extra(include_str!("three/problem_input.txt"));
    println!("Three extra: {}", three_extra);
}
