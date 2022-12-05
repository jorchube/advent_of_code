from src.three import calculate_misplaced_items_priority, calculate_badges_priority

def test_returns_priority_for_one_rucksack_with_only_the_misplaced_items():
    test_input = """
    aa
    """

    priority = calculate_misplaced_items_priority(test_input)

    assert priority == 1

def test_returns_priority_for_many_rucksacks_with_only_the_misplaced_items():
    test_input = """
    aa
    zz
    ZZ
    """

    priority = calculate_misplaced_items_priority(test_input)

    assert priority == 79

def test_returns_priority_for_one_rucksack_with_many_items():
    test_input = """
    zbaDaE
    """

    priority = calculate_misplaced_items_priority(test_input)

    assert priority == 1

def test_returns_priority_for_many_rucksacks_with_many_items():
    test_input = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """

    priority = calculate_misplaced_items_priority(test_input)

    assert priority == 157

def test_return_priority_of_badges_for_a_single_elf_group():
    test_input = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    """

    priority = calculate_badges_priority(test_input)

    assert priority == 18

def test_return_priority_of_badges_for_many_elf_groups():
    test_input = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """

    priority = calculate_badges_priority(test_input)

    assert priority == 70
