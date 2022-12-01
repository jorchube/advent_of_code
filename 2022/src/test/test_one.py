from src.one import parse_input, calculate_elf_max_calories, calculate_top_three_elfs_max_calories

def test_returns_a_list_of_lists_as_a_result_of_parsing_the_input():
    test_input = (
        """
        1
        2

        3

        4
        5
        6
        """
    )

    parsed_input = parse_input(test_input)

    assert parsed_input == [
        [1, 2],
        [3],
        [4, 5, 6]
    ]

def test_calculate_elf_max_calories_for_a_single_elf_with_a_single_item():
    test_input = (
        """
        1
        """
    )

    max_calories = calculate_elf_max_calories(test_input)

    assert max_calories == 1


def test_calculate_elf_max_calories_for_a_single_elf_with_many_items():
    test_input = (
        """
        1
        2
        """
    )

    max_calories = calculate_elf_max_calories(test_input)

    assert max_calories == 3

def test_calculate_elf_max_calories_for_many_elfs_with_many_items():
    test_input = (
        """
        1
        2

        1
        3
        4

        7
        """
    )

    max_calories = calculate_elf_max_calories(test_input)

    assert max_calories == 8

def test_calculate_max_calories_of_top_three_elfs():
    test_input = (
        """
        1
        2

        1
        3
        4

        7

        9
        1
        """
    )

    top_three_max_calories = calculate_top_three_elfs_max_calories(test_input)

    assert top_three_max_calories == 25
