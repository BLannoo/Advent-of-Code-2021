from dataclasses import dataclass
from typing import List


@dataclass()
class Numbers:
    value: int
    marked: bool = False


@dataclass()
class Board:
    grid: List[List[Numbers]]

    @staticmethod
    def parse(str_repr) -> "Board":
        return Board(
            [
                [
                    Numbers(int(cell))
                    for cell in line.split()
                ]
                for line in str_repr.split("\n")
            ]
        )

    def mark(self, number: int) -> "Board":
        for line in self.grid:
            for cell in line:
                if cell.value == number:
                    cell.marked = True
        return self

    def is_won(self) -> bool:
        return (
            self._check_rows_for_win(self.grid)
            or
            self._check_rows_for_win(transpose(self.grid))
        )

    @staticmethod
    def _check_rows_for_win(grid: List[List[Numbers]]) -> bool:
        for line in grid:
            full_line = True
            for cell in line:
                if not cell.marked:
                    full_line = False
                    break
            if full_line:
                return True
        return False

    def unmarked_sum(self):
        return sum(
            cell.value
            for line in self.grid
            for cell in line
            if not cell.marked
        )


def transpose(grid: List[List[any]]) -> List[List[any]]:
    return list(map(list, zip(*grid)))
