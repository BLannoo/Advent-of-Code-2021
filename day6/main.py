from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass(frozen=True)
class School:
    states: Dict[int, int]

    @staticmethod
    def parse(input_file_path: Path) -> "School":
        return School(
            dict(
                Counter(
                    [
                        int(state)
                        for state in input_file_path.read_text().split(",")
                    ]
                )
            )
        )

    def tick(self) -> "School":
        birthing = self.states.get(0, 0)
        states = {
            key - 1: value
            for key, value in self.states.items()
            if key != 0 and value != 0
        }
        states[6] = states.get(6, 0) + birthing
        states[8] = birthing
        return School(states)

    def tick_n(self, n: int) -> "School":
        school = self
        for _ in range(n):
            school = school.tick()
        return school

    def count_fish(self) -> int:
        return sum(
            count
            for count in self.states.values()
        )


def silver(input_file_path: Path) -> int:
    return core(input_file_path, 80)


def gold(input_file_path: Path) -> int:
    return core(input_file_path, 256)


def core(input_file_path: Path, days: int) -> int:
    school = School.parse(input_file_path)
    school = school.tick_n(days)
    return school.count_fish()
