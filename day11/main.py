from dataclasses import dataclass, field
from pathlib import Path
from typing import List


def silver(input_file_path: Path) -> int:
    return OctopusesGrid.parse(input_file_path.read_text()).multi_step(100).flashes


def gold(input_file_path: Path) -> int:
    octopuses_grid = OctopusesGrid.parse(input_file_path.read_text())
    steps = 0
    while not octopuses_grid.all(0):
        steps += 1
        octopuses_grid.step()
    return steps


@dataclass
class Octopus:
    energy: int
    flashed: bool = False


@dataclass
class OctopusesGrid:
    grid: List[List[Octopus]]
    flashes: int = field(default=0, compare=False)

    @property
    def width(self) -> int:
        return len(self.grid[0])

    @property
    def height(self) -> int:
        return len(self.grid)

    @staticmethod
    def parse(description: str) -> "OctopusesGrid":
        cleaned_description = description.replace(" ", "").strip()
        return OctopusesGrid([
            [
                Octopus(int(char))
                for char in line
            ]
            for line in cleaned_description.split("\n")
        ])

    def step(self) -> "OctopusesGrid":
        for line in self.grid:
            for octopus in line:
                octopus.energy += 1

        flashed = True
        while flashed:
            flashed = False
            for y, line in enumerate(self.grid):
                for x, octopus in enumerate(line):
                    if not octopus.flashed and octopus.energy > 9:
                        flashed = True
                        self.flashes += 1
                        octopus.flashed = True
                        for dx in (-1, 0, 1):
                            for dy in (-1, 0, 1):
                                if self.inside(x + dx, y + dy):
                                    self.grid[y + dy][x + dx].energy += 1

        for line in self.grid:
            for octopus in line:
                if octopus.flashed:
                    octopus.energy = 0
                    octopus.flashed = False

        return self

    def inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def __repr__(self):
        return "\n".join(
            "".join(
                str(octopus.energy)
                for octopus in line
            )
            for line in self.grid
        )

    def multi_step(self, steps: int):
        for _ in range(steps):
            self.step()
        return self

    def all(self, energy: int) -> bool:
        for line in self.grid:
            for octopus in line:
                if octopus.energy != energy:
                    return False
        return True
