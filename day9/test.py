from pathlib import Path
from typing import Set

import assertpy
import pytest

from day9.main import silver, gold, Grid, Location

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 15


def test_silver_star():
    assert silver(INPUT_PATH) == 591


@pytest.mark.parametrize(
    "x,y,basin",
    [
        (
            0, 0,
            {
                Location(0, 0),
                Location(0, 1),
                Location(1, 0),
            }
        ),
        (
            5, 0,
            {
                Location(5, 0),
                Location(6, 0),
                Location(6, 1),
                Location(7, 0),
                Location(8, 0),
                Location(8, 1),
                Location(9, 0),
                Location(9, 1),
                Location(9, 2),
            }
        ),
    ]
)
def test_find_basin_from_seed(x: int, y: int, basin: Set[Location]):
    grid = Grid.parse(EXAMPLE_PATH.read_text())
    assertpy.assert_that(
        grid.find_basin_from_seed(Location(x, y))
    ).contains_only(
        *basin
    )


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 1134


def test_gold_star():
    assert gold(INPUT_PATH) == 1113424
