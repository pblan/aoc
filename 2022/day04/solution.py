from aocd import submit

from aoc.utils import read_input, get_session_token


def part1(data):
    count = 0
    for line in data.split("\n"):
        first = set(
            range(int(line.split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)
        )
        second = set(
            range(
                int(line.split(",")[1].split("-")[0]),
                int(line.split(",")[1].split("-")[1]) + 1,
            )
        )
        if first.issubset(second) or second.issubset(first):
            count += 1
    return count


def part2(data):
    count = 0
    for line in data.split("\n"):
        first = set(
            range(int(line.split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)
        )
        second = set(
            range(
                int(line.split(",")[1].split("-")[0]),
                int(line.split(",")[1].split("-")[1]) + 1,
            )
        )
        if first & second:
            count += 1
    return count


if __name__ == "__main__":
    data = read_input(day=4, year=2022)
    submit(
        part1(data), part=1, day=4, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=4, year=2022, session=get_session_token(), reopen=False
    )
