from aocd import submit

from aoc.utils import read_input, get_session_token


def move_tail(head, tail, dx, dy):
    # straight line
    if head[0] == tail[0]:
        if head[1] == tail[1] + 2:
            tail = (tail[0], tail[1] + dy["U"])
        elif head[1] == tail[1] - 2:
            tail = (tail[0], tail[1] + dy["D"])

    if head[1] == tail[1]:
        if head[0] == tail[0] + 2:
            tail = (tail[0] + dx["R"], tail[1])
        elif head[0] == tail[0] - 2:
            tail = (tail[0] + dx["L"], tail[1])

    # weird diagonal
    if head[0] == tail[0] + 2 and head[1] == tail[1] + 1:  # RRU
        tail = (tail[0] + dx["R"], tail[1] + dy["U"])
    elif head[0] == tail[0] + 1 and head[1] == tail[1] + 2:  # RUU
        tail = (tail[0] + dx["R"], tail[1] + dy["U"])
    elif head[0] == tail[0] - 2 and head[1] == tail[1] + 1:  # LLU
        tail = (tail[0] + dx["L"], tail[1] + dy["U"])
    elif head[0] == tail[0] - 1 and head[1] == tail[1] + 2:  # LUU
        tail = (tail[0] + dx["L"], tail[1] + dy["U"])
    elif head[0] == tail[0] + 2 and head[1] == tail[1] - 1:  # RRD
        tail = (tail[0] + dx["R"], tail[1] + dy["D"])
    elif head[0] == tail[0] + 1 and head[1] == tail[1] - 2:  # RDD
        tail = (tail[0] + dx["R"], tail[1] + dy["D"])
    elif head[0] == tail[0] - 2 and head[1] == tail[1] - 1:  # LLD
        tail = (tail[0] + dx["L"], tail[1] + dy["D"])
    elif head[0] == tail[0] - 1 and head[1] == tail[1] - 2:  # LDD
        tail = (tail[0] + dx["L"], tail[1] + dy["D"])

    # real diagonal
    if head[0] == tail[0] + 2 and head[1] == tail[1] + 2:  # RRUU
        tail = (tail[0] + dx["R"], tail[1] + dy["U"])
    elif head[0] == tail[0] - 2 and head[1] == tail[1] + 2:  # LLUU
        tail = (tail[0] + dx["L"], tail[1] + dy["U"])
    elif head[0] == tail[0] + 2 and head[1] == tail[1] - 2:  # RRDD
        tail = (tail[0] + dx["R"], tail[1] + dy["D"])
    elif head[0] == tail[0] - 2 and head[1] == tail[1] - 2:  # LLDD
        tail = (tail[0] + dx["L"], tail[1] + dy["D"])

    return tail


def part1(data):
    start = (0, 0)
    head = start
    tail = start
    visited = set()
    visited.add(start)

    dx = {"L": -1, "R": 1, "U": 0, "D": 0}
    dy = {"L": 0, "R": 0, "U": 1, "D": -1}

    for line in data.splitlines():
        if line.startswith("L"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["L"], head[1] + dy["L"])
                tail = move_tail(head, tail, dx, dy)
                print(line, head, tail)

                visited.add(tail)

        elif line.startswith("R"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["R"], head[1] + dy["R"])
                tail = move_tail(head, tail, dx, dy)
                print(line, head, tail)

                visited.add(tail)

        elif line.startswith("U"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["U"], head[1] + dy["U"])
                tail = move_tail(head, tail, dx, dy)
                print(line, head, tail)

                visited.add(tail)

        elif line.startswith("D"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["D"], head[1] + dy["D"])
                tail = move_tail(head, tail, dx, dy)
                print(line, head, tail)

                visited.add(tail)
    print(len(visited))

    return len(visited)


def part2(data):
    start = (0, 0)
    head = start
    tails = [start for _ in range(10)]
    visited = set()
    visited.add(start)

    dx = {"L": -1, "R": 1, "U": 0, "D": 0}
    dy = {"L": 0, "R": 0, "U": 1, "D": -1}

    for line in data.splitlines():
        if line.startswith("L"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["L"], head[1] + dy["L"])
                for i in range(len(tails)):
                    if i == 0:
                        tails[i] = move_tail(head, tails[i], dx, dy)
                    else:
                        tails[i] = move_tail(tails[i - 1], tails[i], dx, dy)

                    print(line, head, tails)
                    visited.add(tails[-1])

        elif line.startswith("R"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["R"], head[1] + dy["R"])
                for i in range(len(tails)):
                    if i == 0:
                        tails[i] = move_tail(head, tails[i], dx, dy)
                    else:
                        tails[i] = move_tail(tails[i - 1], tails[i], dx, dy)

                    print(line, head, tails)
                    visited.add(tails[-1])

        elif line.startswith("U"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["U"], head[1] + dy["U"])
                for i in range(len(tails)):
                    if i == 0:
                        tails[i] = move_tail(head, tails[i], dx, dy)
                    else:
                        tails[i] = move_tail(tails[i - 1], tails[i], dx, dy)

                    print(line, head, tails)
                    visited.add(tails[-1])

        elif line.startswith("D"):
            for _ in range(int(line[1:])):
                head = (head[0] + dx["D"], head[1] + dy["D"])
                for i in range(len(tails)):
                    if i == 0:
                        tails[i] = move_tail(head, tails[i], dx, dy)
                    else:
                        tails[i] = move_tail(tails[i - 1], tails[i], dx, dy)

                    print(line, head, tails)
                    visited.add(tails[-1])
    print(len(visited))

    return len(visited)


if __name__ == "__main__":
    data = read_input(day=9, year=2022)
    submit(
        part1(data), part=1, day=9, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=9, year=2022, session=get_session_token(), reopen=False
    )
