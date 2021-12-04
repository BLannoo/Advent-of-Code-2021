import re
from pathlib import Path

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
    match = re.match(r"^(\w+) (\d+)$", command)
    return DIRECTIONS[match.group(1)] * int(match.group(2))
