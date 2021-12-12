from pathlib import Path

import pytest

from day8.main import silver, gold, Entry

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 26


def test_silver_star():
    assert silver(INPUT_PATH) == 264


EXAMPLE_ENTRY = Entry("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")


@pytest.mark.parametrize(
    "pattern,digit",
    [
        ("acedgfb", 8),
        # ("cdfbe", 5),
        # ("gcdfa", 2),
        # ("fbcad", 3),
        ("dab", 7),
        # ("cefabd", 9),
        # ("cdfgeb", 6),
        ("eafb", 4),
        # ("cagedb", 0),
        ("ab", 1),
    ]
)
def test_get_digit_pattern_by_length(pattern: str, digit: int):
    sorted_pattern = "".join(sorted(pattern))
    assert EXAMPLE_ENTRY.get_digit_pattern(digit) == sorted_pattern


@pytest.mark.parametrize(
    "actual_segment,displayed_segment",
    [
        ("a", "d"),
        ("b", "e"),
        ("c", "a"),
        ("d", "f"),
        ("e", "g"),
        ("f", "b"),
        ("g", "c"),
    ]
)
def test_get_actual_segment(actual_segment: str, displayed_segment: str):
    assert EXAMPLE_ENTRY.get_actual_segment(displayed_segment) == actual_segment


def test_output_value():
    assert EXAMPLE_ENTRY.output_value() == 5353


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 61229


def test_gold_star():
    assert gold(INPUT_PATH) == 1063760
