class Range:
    def __init__(self, range):
        parts = range.split('-')
        self.start = int(parts[0])
        self.end = int(parts[1])

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return f"{self.start}-{self.end}"

    def fully_overlaps(self, other):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other):
        return not (self.end < other.start or self.start > other.end)

class Pair:
    def __init__(self, range1, range2):
        self.range1 = Range(range1)
        self.range2 = Range(range2)

    def has_full_overlapping_ranges(self):
        return self.range1.fully_overlaps(self.range2) or self.range2.fully_overlaps(self.range1)

    def has_full_or_partial_overlapping_ranges(self):
        return self.range1.overlaps(self.range2) or self.range2.overlaps(self.range1)

    def __str__(self):
        return f"{self.range1},{self.range2}"

def parse_pairs(input):
    pairs = list()
    for line in input.strip().splitlines():
        pair = Pair(*line.strip().split(','))
        pairs.append(pair)

    return pairs

def count_full_overlaps(input):
    pairs = parse_pairs(input)

    overlapping_pairs = list(filter(lambda pair: pair.has_full_overlapping_ranges(), pairs))

    return len(overlapping_pairs)

def count_full_or_partial_overlaps(input):
    pairs = parse_pairs(input)

    overlapping_pairs = list(filter(lambda pair: pair.has_full_or_partial_overlapping_ranges(), pairs))

    return len(overlapping_pairs)

if __name__ == "__main__":
    from input.input_four import INPUT

    full_overlaps = count_full_overlaps(INPUT)
    print(f"full overlaps: {full_overlaps}")

    full_or_partial_overlaps = count_full_or_partial_overlaps(INPUT)
    print(f"full or partial overlaps: {full_or_partial_overlaps}")
