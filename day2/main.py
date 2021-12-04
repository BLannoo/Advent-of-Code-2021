import re
from pathlib import Path

COMMAND_PATTERN = r"^(\w+) (\d+)$"

DIRECTIONS = {
    "forward": complex(1, 0),
    "down": complex(0, 1),
    "up": complex(0, -1),
}


def silver(input_file_path: Path) -> float:
    commands = input_file_path.read_text().split("\n")
    end_point = sum(
        map_to_complex_number(command)
        for command in commands
    )
    return end_point.real * end_point.imag


def map_to_complex_number(command: str) -> complex:
    match = re.match(COMMAND_PATTERN, command)
    return DIRECTIONS[match.group(1)] * int(match.group(2))


def gold(input_file_path: Path) -> float:
    commands = input_file_path.read_text().split("\n")
    position = complex(0, 0)
    aim = 0
    for command in commands:
        match = re.match(COMMAND_PATTERN, command)
        command_type = match.group(1)
        command_magnitude = int(match.group(2))
        if command_type == "forward":
            position += complex(1, aim) * command_magnitude
        elif command_type == "down":
            aim += command_magnitude
        elif command_type == "up":
            aim -= command_magnitude
        else:
            raise Exception(f"invalid: {command_type=}")

    return position.real * position.imag
