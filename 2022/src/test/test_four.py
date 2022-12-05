from src.four import count_full_overlaps, count_full_or_partial_overlaps


def test_returns_full_overlap_count_for_a_pair_without_overlap():
    test_input = """
    1-4,2-5
    """

    overlaps_count = count_full_overlaps(test_input)

    assert overlaps_count == 0

def test_returns_full_overlap_count_for_a_pair_with_overlap():
    test_input = """
    1-4,2-4
    """

    overlaps_count = count_full_overlaps(test_input)

    assert overlaps_count == 1

def test_returns_full_overlap_count_for_many_pairs_with_some_overlaps():
    test_input = """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """

    overlaps_count = count_full_overlaps(test_input)

    assert overlaps_count == 2

def test_returns_full_overlap_count_for_many_pairs_with_big_ranges_with_some_overlaps():
    test_input = """
    1-4,2-4
    123-3456,4321-98765
    555-777,599-699
    1-6,3-4
    3-4,1-9
    1-1,1-1
    """

    overlaps_count = count_full_overlaps(test_input)

    assert overlaps_count == 5

def test_returns_full_or_partial_overlap_count_for_many_pairs_with_some_overlaps():
    test_input = """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """

    overlaps_count = count_full_or_partial_overlaps(test_input)

    assert overlaps_count == 4
