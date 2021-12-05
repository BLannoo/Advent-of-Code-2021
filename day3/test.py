from pathlib import Path

from day3.main import silver, gold

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 198


def test_silver_star():
    assert silver(INPUT_PATH) == 749376


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 230


def test_gold_star():
    assert gold(INPUT_PATH) == 2372923
