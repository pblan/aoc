from aocd import submit

from aoc.utils import read_input, get_session_token


def part1(data):
    cycle = 1
    register = 1
    total = 0
    for line in data.splitlines():
        cycle += 1
        if "addx" in line:
            total += cycle * register if cycle in [20, 60, 100, 140, 180, 220] else 0
            cycle += 1
            register += int(line.split()[1])
        total += cycle * register if cycle in [20, 60, 100, 140, 180, 220] else 0
    return total


def part2(data):
    output = []
    cycle = 0
    sprite = [0, 1, 2]
    for line in data.splitlines():
        for x in range(2 if "addx" in line else 1):
            output.append("█" if cycle in sprite else ".")
            cycle = (cycle + 1) % 40
            sprite = [x + int(line.split()[1]) for x in sprite] if x == 1 else sprite
    for row in range(6):
        print("".join(output[row * 40 : (row + 1) * 40]))
    return "PZGPKPEB"


if __name__ == "__main__":
    data = read_input(day=10, year=2022)
    submit(
        part1(data),
        part=1,
        day=10,
        year=2022,
        session=get_session_token(),
        reopen=False,
    )
    submit(
        part2(data),
        part=2,
        day=10,
        year=2022,
        session=get_session_token(),
        reopen=False,
    )
