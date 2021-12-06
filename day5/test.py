from pathlib import Path

from assertpy import assertpy

from day5.main import Vent, silver, gold

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


def test_check_horizontal_or_vertical():
    assert Vent.parse("0,9 -> 5,9").check_horizontal_or_vertical()
    assert not Vent.parse("8,0 -> 0,8").check_horizontal_or_vertical()
    assert Vent.parse("2,2 -> 2,1").check_horizontal_or_vertical()


def test_generate_locations_vertical():
    assertpy.assert_that(
        Vent.parse("0,9 -> 5,9").generate_locations()
    ).contains(
        (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9),
    )


def test_generate_locations_horizontal():
    assertpy.assert_that(
        Vent.parse("2,2 -> 2,0").generate_locations()
    ).contains(
        (2, 2), (2, 1), (2, 0),
    )


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 5


def test_silver_star():
    assert silver(INPUT_PATH) == 6007


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 12


def test_gold_star():
    assert gold(INPUT_PATH) == 19349
