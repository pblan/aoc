from aocd import submit

from aoc.utils import read_input, get_session_token

# given:
# [T] [V]                     [W]
# [V] [C] [P] [D]             [B]
# [J] [P] [R] [N] [B]         [Z]
# [W] [Q] [D] [M] [T]     [L] [T]
# [N] [J] [H] [B] [P] [T] [P] [L]
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9


def part1(data):
    # 9 pegs
    pegs = [[], [], [], [], [], [], [], [], []]

    for i, line in enumerate(data.split("\n")):
        # if line starts with empty space, skip
        if line[0] == " ":
            break
        for j in range(0, len(line), 4):
            if line[j] != " ":
                pegs[j // 4].append(line[j + 1])

    # reverse the pegs
    pegs = [peg[::-1] for peg in pegs]

    i += 2

    for line in data.split("\n")[i:]:
        move = line.split(" ")
        x = int(move[1])
        source = int(move[3])
        destination = int(move[5])
        # move x from source to to
        for _ in range(x):
            pegs[destination - 1].append(pegs[source - 1].pop())

    # return string of each last item and remove whitespace
    return "".join([peg[-1] for peg in pegs]).replace(" ", "")


def part2(data):
    # 9 pegs
    pegs = [[], [], [], [], [], [], [], [], []]

    for i, line in enumerate(data.split("\n")):
        # if line starts with empty space, skip
        if line[0] == " ":
            break
        for j in range(0, len(line), 4):
            if line[j] != " ":
                pegs[j // 4].append(line[j + 1])

    # reverse the pegs
    pegs = [peg[::-1] for peg in pegs]

    i += 2

    for line in data.split("\n")[i:]:
        move = line.split(" ")
        x = int(move[1])
        source = int(move[3])
        destination = int(move[5])

        pegs[destination - 1].extend(pegs[source - 1][-x:])
        pegs[source - 1] = pegs[source - 1][:-x]

    return "".join([peg[-1] for peg in pegs]).replace(" ", "")


if __name__ == "__main__":
    data = read_input(day=5, year=2022)
    submit(
        part1(data), part=1, day=5, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=5, year=2022, session=get_session_token(), reopen=False
    )
