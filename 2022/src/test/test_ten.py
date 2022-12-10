import pytest

from src.ten import CPU, CRT

def test_returns_x_values_for_a_not_run_program():
    assert CPU("").get_x_values() == []

def test_returns_x_values_for_one_noop():
    input = "noop"

    cpu = CPU(input)
    cpu.run()

    assert cpu.get_x_values() == [1]

def test_returns_x_values_for_many_noops():
    input = """
noop
noop
noop
"""

    cpu = CPU(input)
    cpu.run()

    assert cpu.get_x_values() == [1, 1, 1]

@pytest.mark.parametrize(("input", "expected_result"), [
    ("addx 1", [1, 2]),
    ("addx 3", [1, 4]),
    ("addx -1", [1, 0]),
    ("addx -123", [1, -122])
])
def test_returns_x_values_for_one_addx(input, expected_result):
    cpu = CPU(input)
    cpu.run()

    assert cpu.get_x_values() == expected_result

def test_returns_x_values_for_many_addx():
    input = """
addx 1
addx 3
addx -1
addx -123
"""

    cpu = CPU(input)
    cpu.run()

    assert cpu.get_x_values() == [1, 2, 2, 5, 5, 4, 4, -119]

def test_return_x_values_for_example_input():
    input = """
noop
addx 3
addx -5
"""
    cpu = CPU(input)
    cpu.run()

    assert cpu.get_x_values() == [1, 1, 4, 4, -1]

def test_returns_signal_strength_during_specific_cycles_and_its_sum():
    input = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

    cpu = CPU(input)
    cpu.run()

    assert cpu.get_signal_strength_during_key_cycles() == [420, 1140, 1800, 2940, 2880, 3960]
    assert cpu.get_signal_strength_sum() == 13140

def test_returns_crt_image():
    input = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

    cpu = CPU(input)
    cpu.run()

    crt = CRT()

    assert crt.draw(cpu.get_x_values()) == """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
