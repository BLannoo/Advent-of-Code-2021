from pathlib import Path

import pytest
from assertpy import assertpy

from day14.main import silver, Polymerizer

EXAMPLE_PATH = Path(__file__).parent / "example.txt"
INPUT_PATH = Path(__file__).parent / "input.txt"


@pytest.mark.parametrize(
    "steps,expected",
    [
        (0, "NNCB"),
        (1, "NCNBCHB"),
        (2, "NBCCNBBBCBHCB"),
        (3, "NBBBCNCCNBBNBNBBCHBHHBCHB"),
        (4, "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"),
    ]
)
def test_polymerization(steps: int, expected: str):
    assert Polymerizer.parse(EXAMPLE_PATH).polymerize_n_times(steps).polymer_str() == expected


def test_count_monomers():
    polymerizer = Polymerizer.parse(EXAMPLE_PATH).polymerize_n_times(10)
    assertpy.assert_that(
        polymerizer.count()
    ).is_equal_to(
        {
            "B": 1749,
            "C": 298,
            "H": 161,
            "N": 865,
        }
    )


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 1588


def test_silver_star():
    assert silver(INPUT_PATH) == 3095
