from pathlib import Path

import pytest

from day11.main import silver, OctopusesGrid, gold

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


@pytest.mark.parametrize(
    "before_desc,after_desc",
    [
        (
            """
            11111
            19991
            19191
            19991
            11111
            """,
            """
            34543
            40004
            50005
            40004
            34543
            """
        ),
        (
            """
            6594254334
            3856965822
            6375667284
            7252447257
            7468496589
            5278635756
            3287952832
            7993992245
            5957959665
            6394862637
            """,
            """
            8807476555
            5089087054
            8597889608
            8485769600
            8700908800
            6600088989
            6800005943
            0000007456
            9000000876
            8700006848
            """
        ),
    ]
)
def test_step(before_desc: str, after_desc: str):
    assert OctopusesGrid.parse(before_desc).step() == OctopusesGrid.parse(after_desc)


def test_flash_counts():
    assert OctopusesGrid.parse(EXAMPLE_PATH.read_text()).multi_step(10).flashes == 204


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 1656


def test_silver_star():
    assert silver(INPUT_PATH) == 1691


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 195


def test_gold_star():
    assert gold(INPUT_PATH) == 216
