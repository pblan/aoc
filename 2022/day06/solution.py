from aocd import submit

from aoc.utils import read_input, get_session_token


def part1(data):
    window_size = 4
    for i in range(len(data) - window_size):
        if len(set(data[i : i + window_size])) == window_size:
            return i + window_size


def part2(data):
    window_size = 14
    for i in range(len(data) - window_size):
        if len(set(data[i : i + window_size])) == window_size:
            return i + window_size


if __name__ == "__main__":
    data = read_input(day=6, year=2022)
    submit(
        part1(data), part=1, day=6, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=6, year=2022, session=get_session_token(), reopen=False
    )
