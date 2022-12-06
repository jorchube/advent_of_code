import pytest
from src.six import count_characters_processed_before_first_packet_marker, count_characters_processed_before_first_message_marker

@pytest.mark.parametrize(("input", "expected_result"), [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
])
def test_returns_count_of_characters_processed_before_first_marker(input, expected_result):
    result = count_characters_processed_before_first_packet_marker(input)

    assert expected_result == result

@pytest.mark.parametrize(("input", "expected_result"), [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
])
def test_returns_count_of_characters_processed_before_first_message(input, expected_result):
    result = count_characters_processed_before_first_message_marker(input)

    assert expected_result == result
