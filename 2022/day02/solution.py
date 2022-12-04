from aocd import submit

from aoc.utils import read_input, get_session_token

# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

OUTCOME = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}


def part1(data):
    return sum(
        [(POINTS[move[2]] + OUTCOME[move[0]][move[2]]) for move in data.split("\n")]
    )


# Anyway, the second column says how the round needs to end:
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

BEATING = {"A": "Y", "B": "Z", "C": "X"}
LOSING = {"A": "Z", "B": "X", "C": "Y"}
DRAW = {"A": "X", "B": "Y", "C": "Z"}


def part2(data):
    return sum(
        [
            (
                POINTS[BEATING[move[0]]] + OUTCOME[move[0]][BEATING[move[0]]]
                if move[2] == "Z"
                else POINTS[DRAW[move[0]]] + OUTCOME[move[0]][DRAW[move[0]]]
                if move[2] == "Y"
                else POINTS[LOSING[move[0]]] + OUTCOME[move[0]][LOSING[move[0]]]
            )
            for move in data.split("\n")
        ]
    )


if __name__ == "__main__":
    data = read_input(day=2, year=2022)
    submit(
        part1(data), part=1, day=2, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=2, year=2022, session=get_session_token(), reopen=False
    )
