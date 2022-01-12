from pathlib import Path

from day15.main import silver

EXAMPLE_PATH = Path(__file__).parent / "example.txt"
INPUT_PATH = Path(__file__).parent / "input.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 40


def test_silver_star():
    assert silver(INPUT_PATH) == 388
