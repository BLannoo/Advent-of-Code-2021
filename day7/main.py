from pathlib import Path


def silver(input_file_path: Path) -> int:
    positions = sorted([
        int(number)
        for number in input_file_path.read_text().split(",")
    ])

    front = positions.pop(-1)
    front_count = 1
    back = positions.pop(0)
    back_count = 1

    fuel = 0

    while front != back:
        while len(positions) > 0 and positions[-1] == front:
            positions.pop(-1)
            front_count += 1
        while len(positions) > 0 and positions[0] == back:
            positions.pop(0)
            back_count += 1
        if back_count > front_count:
            fuel += front_count
            front -= 1
        else:
            fuel += back_count
            back += 1

    return fuel
