from pathlib import Path

from day7.main import silver

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 37


def test_silver_star():
    assert silver(INPUT_PATH) == 328187
