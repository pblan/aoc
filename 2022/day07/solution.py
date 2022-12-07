from aocd import submit

from aoc.utils import read_input, get_session_token


def part1(data):
    current_dir = "/"
    dir_structure = {
        current_dir: 0
    }  # key is directory path, value is size of directory

    for line in data.splitlines():
        # skip first line because hardcoded
        if line == "$ cd /":
            continue

        # command
        if line.startswith("$"):
            if line == "$ ls":
                continue

            if line == "$ cd ..":
                current_dir = "/".join(current_dir.split("/")[:-1])
                continue
            else:
                current_dir = current_dir + "/" + line.split(" ")[-1]

            if current_dir not in dir_structure:
                dir_structure[current_dir] = 0
        else:
            # directory
            if line.startswith("dir"):
                dir_name = current_dir + "/" + line.split(" ")[1]
                if dir_name not in dir_structure:
                    dir_structure[dir_name] = 0
            # file
            else:
                file_size = int(line.split(" ")[0])
                dir_structure[current_dir] += file_size

    actual_sizes = {}
    for dir_name, dir_size in dir_structure.items():
        actual_sizes[dir_name] = sum(
            [
                sub_dir_size
                for sub_dir_name, sub_dir_size in dir_structure.items()
                if sub_dir_name.startswith(dir_name)
            ]
        )

    shrinked_dir_sum = 0
    for dir_name, dir_size in actual_sizes.items():
        if dir_size < 100000:
            shrinked_dir_sum += dir_size

    return shrinked_dir_sum


def part2(data):
    total_disk_size = 70000000
    required_disk_size = 30000000

    current_dir = "/"
    dir_structure = {
        current_dir: 0
    }  # key is directory path, value is size of directory

    for line in data.splitlines():
        # skip first line because hardcoded
        if line == "$ cd /":
            continue

        # command
        if line.startswith("$"):
            if line == "$ ls":
                continue

            if line == "$ cd ..":
                current_dir = "/".join(current_dir.split("/")[:-1])
                continue
            else:
                current_dir = current_dir + "/" + line.split(" ")[-1]

            if current_dir not in dir_structure:
                dir_structure[current_dir] = 0
        else:
            # directory
            if line.startswith("dir"):
                dir_name = current_dir + "/" + line.split(" ")[1]
                if dir_name not in dir_structure:
                    dir_structure[dir_name] = 0
            # file
            else:
                file_size = int(line.split(" ")[0])
                dir_structure[current_dir] += file_size

    actual_sizes = {}
    for dir_name, dir_size in dir_structure.items():
        actual_sizes[dir_name] = sum(
            [
                sub_dir_size
                for sub_dir_name, sub_dir_size in dir_structure.items()
                if sub_dir_name.startswith(dir_name)
            ]
        )

    sorted_dirs = sorted(
        [(dir_name, dir_size) for dir_name, dir_size in actual_sizes.items()],
        key=lambda x: x[1],
    )

    current_used_disk_size = actual_sizes["/"]
    total_unused = total_disk_size - current_used_disk_size
    threshold = required_disk_size - total_unused

    smallest_dir = min(
        [
            (dir_name, dir_size)
            for dir_name, dir_size in sorted_dirs
            if dir_size > threshold
        ],
        key=lambda x: x[1],
    )

    return smallest_dir[1]


if __name__ == "__main__":
    data = read_input(day=7, year=2022)
    submit(
        part1(data), part=1, day=7, year=2022, session=get_session_token(), reopen=False
    )
    submit(
        part2(data), part=2, day=7, year=2022, session=get_session_token(), reopen=False
    )
