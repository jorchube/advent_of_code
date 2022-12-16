from src.fifteen import parse_input, get_positions_without_beacon, get_positions_without_beacon_at_row

def test_it_parses_a_sensor():
    input = """
Sensor at x=3696849, y=2604845: closest beacon is at x=3702627, y=2598480
"""

    sensors = parse_input(input)

    assert sensors[0].x == 3696849
    assert sensors[0].y == 2604845
    assert sensors[0].beacon.x == 3702627
    assert sensors[0].beacon.y == 2598480

def test_it_parses_many_sensors():
    input = """
Sensor at x=3696849, y=2604845: closest beacon is at x=3702627, y=2598480
Sensor at x=2357787, y=401688: closest beacon is at x=1686376, y=-104303
"""

    sensors = parse_input(input)

    assert sensors[0].x == 3696849
    assert sensors[0].y == 2604845
    assert sensors[0].beacon.x == 3702627
    assert sensors[0].beacon.y == 2598480
    assert sensors[1].x == 2357787
    assert sensors[1].y == 401688
    assert sensors[1].beacon.x == 1686376
    assert sensors[1].beacon.y == -104303

def test_it_returns_positions_not_containing_a_beacon_for_distance_1():
    input = """
Sensor at x=9, y=16: closest beacon is at x=8, y=16
"""

    sensors = parse_input(input)
    positions_without_beacon = get_positions_without_beacon(sensors)

    assert set(positions_without_beacon) == {
        (10, 16),
        (9, 15),
        (9, 17)
    }

def test_it_returns_positions_not_containing_a_beacon_for_distance_2():
    input = """
Sensor at x=9, y=16: closest beacon is at x=8, y=17
"""

    sensors = parse_input(input)
    positions_without_beacon = get_positions_without_beacon(sensors)

    assert set(positions_without_beacon) == {
        (9, 14),
        (9, 15),
        (9, 17),
        (9, 18),
        (7, 16),
        (8, 16),
        (10, 16),
        (11, 16),
        (8, 15),
        (10, 15),
        (10, 17)
    }

def test_it_returns_positions_not_containing_a_beacon_for_negative_coordinates():
    input = """
Sensor at x=0, y=1: closest beacon is at x=-1, y=1
"""

    sensors = parse_input(input)
    positions_without_beacon = get_positions_without_beacon(sensors)

    assert set(positions_without_beacon) == {
        (1, 1),
        (0, 0),
        (0, 2),
    }

def test_returns_positions_not_containing_a_beacon_in_a_given_row():
    input = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

    sensors = parse_input(input)
    positions_without_beacon = get_positions_without_beacon_at_row(sensors, 10)

    assert len(positions_without_beacon) == 26
