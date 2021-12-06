from pathlib import Path

import assertpy

from day6.main import silver, School, core, gold

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


def test_example_day_1():
    assertpy.assert_that(
        School.parse(EXAMPLE_PATH).tick().states
    ).contains_entry(
        {0: 1}
    ).contains_entry(
        {1: 1}
    ).contains_entry(
        {2: 2}
    ).contains_entry(
        {3: 1}
    )


def test_example_day_2():
    assertpy.assert_that(
        School.parse(EXAMPLE_PATH).tick_n(2).states
    ).is_equal_to(
        {0: 1, 1: 2, 2: 1, 6: 1, 8: 1}
    )


def test_example_day_4():
    assertpy.assert_that(
        School.parse(EXAMPLE_PATH).tick_n(4).states
    ).is_equal_to(
        {0: 1, 4: 1, 5: 1, 6: 3, 7: 1, 8: 2}
    )


def test_count_fish():
    assert School.parse(EXAMPLE_PATH).count_fish() == 5


def test_18_days():
    assert core(EXAMPLE_PATH, 18) == 26


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 5934


def test_silver_star():
    assert silver(INPUT_PATH) == 385391


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 26984457539


def test_gold_star():
    assert gold(INPUT_PATH) == 1728611055389
