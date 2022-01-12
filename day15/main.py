from dataclasses import dataclass
from pathlib import Path

from sortedcontainers import SortedList


@dataclass(order=True)
class PathEndPoint:
    risk: int
    x: int
    y: int


def silver(input_path: Path) -> int:
    grid = [
        [
            int(char)
            for char in line
        ]
        for line in input_path.read_text().split("\n")
    ]

    visited = [
        [
            False
            for _ in line
        ]
        for line in input_path.read_text().split("\n")
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
