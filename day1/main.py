from pathlib import Path
from typing import List


def silver(input_file_path: Path) -> int:
    depths = read_input(input_file_path)
    return count_increments(depths)


def gold(input_file_path: Path) -> int:
    depths = read_input(input_file_path)
    windows = sliding_sum(depths)
    return count_increments(windows)


def sliding_sum(depths: List[int]) -> List[int]:
    return [
        previous_depth + current_depth + next_depth
        for previous_depth, current_depth, next_depth in zip(
            depths[:-2], depths[1:-1], depths[2:]
        )
    ]


def count_increments(depths: List[int]) -> int:
    return len([
        1
        for previous_depth, next_depth in zip(depths[:-1], depths[1:])
        if previous_depth - next_depth < 0
    ])


def read_input(input_file_path: Path) -> List[int]:
    return [
        int(depth)
        for depth in input_file_path.read_text().split("\n")
    ]
