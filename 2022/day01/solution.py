from aocd import submit

from aoc.utils import read_input, get_session_token


def part1(data):
    return max([sum([int(x) for x in line.split("\n")]) for line in data.split("\n\n")])


def part2(data):
    sums = [sum([int(x) for x in line.split("\n")]) for line in data.split("\n\n")]
    sums.sort()
    return sums[-1] + sums[-2] + sums[-3]


if __name__ == "__main__":
    data = read_input(day=1, year=2022)
    submit(
        part1(data), part=1, day=1, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=1, year=2022, session=get_session_token(), reopen=False
    )
