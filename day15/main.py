from dataclasses import dataclass
from pathlib import Path
from typing import List

from sortedcontainers import SortedList


@dataclass(order=True)
class PathEndPoint:
    risk: int
    x: int
    y: int


def silver(input_path: Path) -> int:
    return core(parse_grid(input_path))


def gold(input_path: Path) -> int:
    grid = parse_grid(input_path)
    return core(extended_grid(grid))


def extended_grid(grid):
    height = len(grid)
    width = len(grid[0])
    return [
        [
            extended_risk(grid, x, y)
            for x in range(width * 5)
        ]
        for y in range(height * 5)
    ]


def extended_risk(grid: List[List[int]], x: int, y: int) -> int:
    height = len(grid)
    width = len(grid[0])
    reference_value = grid[y % height][x % width]
    increased_value = reference_value + y // height + x // width
    return (increased_value - 1) % 9 + 1


def parse_grid(input_path):
    return [
        [
            int(char)
            for char in line
        ]
        for line in input_path.read_text().split("\n")
    ]


def core(grid: List[List[int]]) -> int:
    visited = [
        [
            False
            for _ in line
        ]
        for line in grid
    ]

    height = len(grid)
    width = len(grid[0])

    partial_paths = SortedList([PathEndPoint(x=0, y=0, risk=0)])
    visited[0][0] = True

    while True:
        partial_path = partial_paths.pop(0)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            new_x = partial_path.x + dx
            if not 0 <= new_x <= width - 1:
                continue
            new_y = partial_path.y + dy
            if not 0 <= new_y <= height - 1:
                continue
            if visited[new_y][new_x]:
                continue
            new_risk = partial_path.risk + grid[new_y][new_x]
            if new_x == width - 1 and new_y == height - 1:
                return new_risk
            partial_paths.add(
                PathEndPoint(risk=new_risk, x=new_x, y=new_y)
            )
            visited[new_y][new_x] = True
