from pathlib import Path
from typing import Dict

import pytest
from assertpy import assertpy

from day14.main import polymerize, core

EXAMPLE_PATH = Path(__file__).parent / "example.txt"
INPUT_PATH = Path(__file__).parent / "input.txt"


@pytest.mark.parametrize(
    "polymerization_times,expected",
    [
        (0, {'N': 2, 'C': 1, 'B': 1, 'H': 0}),  # NNCB
        (1, {'N': 2, 'C': 2, 'B': 2, 'H': 1}),  # NCNBCHB
        (10, {"B": 1749, "C": 298, "H": 161, "N": 865}),
    ]
)
def test_polymer_count_pairs(polymerization_times: int, expected: Dict[str, int]):
    assertpy.assert_that(
        polymerize(EXAMPLE_PATH, polymerization_times)
    ).is_equal_to(
        expected
    )


def test_silver_example():
    assert core(EXAMPLE_PATH, 10) == 1588


def test_silver_star():
    assert core(INPUT_PATH, 10) == 3095


def test_gold_example():
    assert core(EXAMPLE_PATH, 40) == 2188189693529


def test_gold_star():
    assert core(INPUT_PATH, 40) == 3152788426516
