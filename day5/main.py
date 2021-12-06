import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Callable


@dataclass(frozen=True)
class Vent:
    x1: int
    y1: int
    x2: int
    y2: int

    @staticmethod
    def parse(description: str) -> "Vent":
        match = re.match(r"^(\d+),(\d+) -> (\d+),(\d+)$", description)
        return Vent(
            *[
                int(match)
                for match in match.groups()
            ]
        )

    def check_horizontal_or_vertical(self) -> bool:
        return (
            self.x1 == self.x2
            or
            self.y1 == self.y2
        )

    def generate_locations(self) -> List[Tuple[int, int]]:
        x_dir = int(math.copysign(1, self.x2 - self.x1))
        y_dir = int(math.copysign(1, self.y2 - self.y1))
        if self.x1 == self.x2:
            return [
                (self.x1, y)
                for y in range(self.y1, self.y2 + y_dir, y_dir)
            ]
        elif self.y1 == self.y2:
            return [
                (x, self.y1)
                for x in range(self.x1, self.x2 + x_dir, x_dir)
            ]
        else:
            return list(zip(
                range(self.x1, self.x2 + x_dir, x_dir),
                range(self.y1, self.y2 + y_dir, y_dir),
            ))


def silver(input_file_path: Path) -> int:
    return core(input_file_path, vent_filter=lambda vent: vent.check_horizontal_or_vertical())


def gold(input_file_path: Path) -> int:
    return core(input_file_path, vent_filter=lambda vent: True)


def core(input_file_path: Path, vent_filter: Callable[[Vent], bool]) -> int:
    vents = [
        Vent.parse(vent_description)
        for vent_description in input_file_path.read_text().split("\n")
    ]

    points = [
        point
        for vent in vents
        if vent_filter(vent)
        for point in vent.generate_locations()
    ]

    return len([
        1
        for count in Counter(points).values()
        if count >= 2
    ])
