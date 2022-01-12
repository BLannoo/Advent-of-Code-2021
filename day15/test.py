from pathlib import Path

import pytest

from day15.main import silver, gold, extended_risk, parse_grid

EXAMPLE_PATH = Path(__file__).parent / "example.txt"
INPUT_PATH = Path(__file__).parent / "input.txt"
EXTENDED_EXAMPLE_PATH = Path(__file__).parent / "extended_example.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 40


def test_silver_star():
    assert silver(INPUT_PATH) == 388


@pytest.mark.parametrize(
    "x, y",
    [
        (0, 0),
        (0, 49),
        (49, 0),
        (49, 49),
        (0, 25),
        (25, 0),
        (25, 25),
    ]
)
def test_extended_risk(x: int, y: int) -> None:
    grid = parse_grid(EXAMPLE_PATH)
    extended_grid = parse_grid(EXTENDED_EXAMPLE_PATH)
    assert extended_risk(grid, x, y) == extended_grid[y][x]


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 315


def test_gold_star():
    assert gold(INPUT_PATH) == 2819
