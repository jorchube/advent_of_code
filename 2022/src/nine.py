import re

class RopeSegment:
    def __init__(self, initial_x, initial_y, next_segment=None):
        self.x = initial_x
        self.y = initial_y
        self.positions = list()
        self._save_position()

        self.next_segment = next_segment

    def get_position(self):
        return self.x, self.y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        self._save_position()

        if not self.next_segment or self.next_segment.is_adjacent_to(self):
            return

        distance_x, distance_y = self.next_segment.distance_to(self)
        move_x = distance_x/abs(distance_x) if distance_x else 0
        move_y = distance_y/abs(distance_y) if distance_y else 0

        self.next_segment.move(move_x, move_y)

    def _save_position(self):
        position = tuple(self.get_position())
        if position not in self.positions:
            self.positions.append(position)

    def is_adjacent_to(self, other):
        dist_x, dist_y = self.distance_to(other)
        return abs(dist_x) <= 1 and abs(dist_y) <= 1

    def distance_to(self, other):
        return other.x - self.x, other.y - self.y

class Rope:
    def __init__(self):
        self.tail = RopeSegment(0, 0)
        self.head = RopeSegment(0, 0, next_segment=self.tail)

    def get_head_position(self):
        return self.head.get_position()

    def get_tail_position(self):
        return self.tail.get_position()

    def bulk_move_head(self, moves):
        for move in moves:
            self.move_head(*move)

    def move_head(self, delta_x, delta_y):
        self.head.move(delta_x, delta_y)

    def count_tail_positions(self):
        return len(self.tail.positions)

class LongRope(Rope):
    def __init__(self, segments=10):
        self.tail = RopeSegment(0, 0)
        segment = self.tail
        for _ in range(segments - 2):
            new_segment = RopeSegment(0, 0, next_segment=segment)
            segment = new_segment
        self.head = RopeSegment(0, 0, segment)

def parse_input(input):
    lines = input.strip().splitlines()

    moves = list()

    right_move = re.compile(r"R (\d+)")
    left_move = re.compile(r"L (\d+)")
    up_move = re.compile(r"U (\d+)")
    down_move = re.compile(r"D (\d+)")

    for line in lines:
        if right_move.match(line):
            base_move = [(1, 0)]
            times = int(right_move.match(line).group(1))

        if left_move.match(line):
            base_move = [(-1, 0)]
            times = int(left_move.match(line).group(1))

        if up_move.match(line):
            base_move = [(0, 1)]
            times = int(up_move.match(line).group(1))

        if down_move.match(line):
            base_move = [(0, -1)]
            times = int(down_move.match(line).group(1))

        moves.extend(base_move * times)

    return moves

if __name__ == "__main__":
    from input.input_nine import INPUT

    bulk_moves = parse_input(INPUT)

    rope = Rope()
    rope.bulk_move_head(bulk_moves)
    num_visited_tail_positions = rope.count_tail_positions()
    print(f"num_visited_tail_positions: {num_visited_tail_positions}")


    long_rope = LongRope()
    long_rope.bulk_move_head(bulk_moves)
    num_visited_tail_positions_for_long_rope = long_rope.count_tail_positions()
    print(f"num_visited_tail_positions_for_long_rope: {num_visited_tail_positions_for_long_rope}")
