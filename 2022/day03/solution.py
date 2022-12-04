from aocd import submit

from aoc.utils import read_input, get_session_token

value = lambda v: ord(v) - 96 if v.islower() else ord(v) - 64 + 26


def part1(data):
    sum = 0
    for line in data.split("\n"):
        first = line[: int(len(line) / 2)]
        second = line[int(len(line) / 2) :]
        for i in range(len(first)):
            if first[i] in second:
                sum += value(first[i])
                break

    return sum


def part2(data):
    sum = 0
    for i, line in enumerate(data.split("\n")):
        if i % 3 == 0:
            first = set(line)
        elif i % 3 == 1:
            second = set(line)
        else:
            third = set(line)
            sum += value(list(first & second & third)[0])

    return sum


if __name__ == "__main__":
    data = read_input(day=3, year=2022)
    submit(
        part1(data), part=1, day=3, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=3, year=2022, session=get_session_token(), reopen=False
    )
