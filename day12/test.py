from pathlib import Path

import pytest

from day12.main import silver, gold

INPUT_PATH = Path(__file__).parent / "input.txt"


@pytest.mark.parametrize(
    "input_file_name,num_paths",
    [
        ("example_1.txt", 10),
        ("example_2.txt", 19),
        ("example_3.txt", 226),
    ]
)
def test_silver_example(input_file_name: str, num_paths: int):
    assert silver(Path(__file__).parent / input_file_name) == num_paths


def test_silver_star():
    assert silver(INPUT_PATH) == 5212


@pytest.mark.parametrize(
    "input_file_name,num_paths",
    [
        ("example_1.txt", 36),
        ("example_2.txt", 103),
        ("example_3.txt", 3509),
    ]
)
def test_gold_example(input_file_name: str, num_paths: int):
    assert gold(Path(__file__).parent / input_file_name) == num_paths


def test_gold_star():
    assert gold(INPUT_PATH) == 5212
