from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import List, Set


@dataclass(frozen=True)
class Location:
    x: int
    y: int

    def __add__(self, other: "Location") -> "Location":
        return Location(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def neighbours(self) -> Set["Location"]:
        return {
            self + direction
            for direction in DIRECTIONS
        }


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

    def find_basin_from_seed(self, location: Location) -> Set[Location]:
        to_expand = {location}
        basin = {location}
        while len(to_expand) > 0:
            current_location = to_expand.pop()
            neighbours = current_location.neighbours()
            basin_neighbours = self.non_9_locations().intersection(neighbours)
            to_expand = to_expand.union(basin_neighbours - basin)
            basin = basin.union(basin_neighbours)
        return basin

    def non_9_locations(self) -> Set[Location]:
        return {
            Location(x, y)
            for x in range(self.width)
            for y in range(self.height)
            if self.get(Location(x, y)) != 9
        }


def silver(input_file_path: Path) -> int:
    grid = Grid.parse(input_file_path.read_text())
    return grid.sum_risk_levels()


def gold(input_file_path: Path) -> int:
    grid = Grid.parse(input_file_path.read_text())

    basins = []
    potential_seeds = grid.non_9_locations()
    while len(potential_seeds) > 0:
        seed_location = potential_seeds.pop()
        new_basin = grid.find_basin_from_seed(seed_location)
        basins.append(new_basin)
        potential_seeds -= new_basin

    basins.sort(key=lambda basin: len(basin))

    return len(basins[-1]) * len(basins[-2]) * len(basins[-3])
