from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class Location:
    x: int
    y: int

    def __add__(self, other: "Location") -> "Location":
        return Location(
            x=self.x + other.x,
            y=self.y + other.y,
        )


DIRECTIONS = (
    Location(0, 1),
    Location(0, -1),
    Location(1, 0),
    Location(-1, 0),
)


@dataclass(frozen=True)
class Grid:
    grid: List[List[int]]

    def get(self, location: Location) -> int:
        return self.grid[location.y][location.x]

    @property
    def height(self) -> int:
        return len(self.grid)

    @property
    def width(self) -> int:
        return len(self.grid[0])

    def sum_risk_levels(self):
        return sum(
            [
                self.get_risk_level(low_point)
                for low_point in self.low_points()
            ]
        )

    def get_risk_level(self, location: Location) -> int:
        return self.get(location) + 1

    def low_points(self):
        return [
            Location(x, y)
            for x in range(self.width)
            for y in range(self.height)
            if self.is_low_point(Location(x, y))
        ]

    def is_low_point(self, location: Location) -> bool:
        for direction in DIRECTIONS:
            neighbour = location + direction
            if (
                self.is_inside(neighbour)
                and
                (self.get(neighbour) <= self.get(location))
            ):
                return False
        return True

    def is_inside(self, location: Location) -> bool:
        return (
            (0 <= location.x < self.width)
            and
            (0 <= location.y < self.height)
        )

    @staticmethod
    def parse(description: str) -> "Grid":
        return Grid(
            [
                [
                    int(cell)
                    for cell in line
                ]
                for line in description.split("\n")
            ]
        )


def silver(input_file_path: Path) -> int:
    grid = Grid.parse(input_file_path.read_text())
    return grid.sum_risk_levels()
