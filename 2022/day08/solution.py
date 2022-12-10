from aocd import submit

from aoc.utils import read_input, get_session_token


def part1(data):
    count = 0
    for i, line in enumerate(data.splitlines()):
        for j, char in enumerate(line):
            if all([int(char) > int(data.splitlines()[i][k]) for k in range(j)]) or all(
                [int(char) > int(data.splitlines()[k][j]) for k in range(i)]
                or all(
                    [
                        int(char) > int(data.splitlines()[i][k])
                        for k in range(j + 1, len(line))
                    ]
                )
                or all(
                    [
                        int(char) > int(data.splitlines()[k][j])
                        for k in range(i + 1, len(data.splitlines()))
                    ]
                )
            ):
                count += 1

    return count


def part2(data):
    cur_max = {0: 0, 1: 0, 2: 0, 3: 0}  # (left, right, up, down)
    for i, line in enumerate(data.splitlines()):
        for j, char in enumerate(line):
            cur = data.splitlines()[i][j]
            count = {0: 0, 1: 0, 2: 0, 3: 0}
            for k in range(j):
                if int(cur) > int(data.splitlines()[i][j - k - 1]):
                    count[0] += 1
                else:
                    count[0] += 1
                    break
            for k in range(len(line) - j - 1):
                if int(cur) > int(data.splitlines()[i][j + k + 1]):
                    count[1] += 1
                else:
                    count[1] += 1
                    break
            for k in range(i):
                if int(cur) > int(data.splitlines()[i - k - 1][j]):
                    count[2] += 1
                else:
                    count[2] += 1
                    break
            for k in range(len(data.splitlines()) - i - 1):
                if int(cur) > int(data.splitlines()[i + k + 1][j]):
                    count[3] += 1
                else:
                    count[3] += 1
                    break
            # if product of count is greater than cur_max, update cur_max
            if (
                count[0] * count[1] * count[2] * count[3]
                > cur_max[0] * cur_max[1] * cur_max[2] * cur_max[3]
            ):
                cur_max = count

    return cur_max[0] * cur_max[1] * cur_max[2] * cur_max[3]


if __name__ == "__main__":
    data = read_input(day=8, year=2022)
    # submit(
    #     part1(data), part=1, day=8, year=2022, session=get_session_token(), reopen=False
    # )
    submit(
        part2(data), part=2, day=8, year=2022, session=get_session_token(), reopen=False
    )
