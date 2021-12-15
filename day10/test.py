from pathlib import Path

import pytest

from day10.main import silver, first_corrupted_character

INPUT_PATH = Path(__file__).parent / "input.txt"
EXAMPLE_PATH = Path(__file__).parent / "example.txt"


@pytest.mark.parametrize(
    "character,line",
    [
        ("}", "{([(<{}[<>[]}>{[]{[(<()>"),
        (")", "[[<[([]))<([[{}[[()]]]"),
        ("]", "[{[{({}]{}}([{[{{{}}([]"),
        (")", "[<(<(<(<{}))><([]([]()"),
        (">", "<{([([[(<>()){}]>(<<{{"),
        ("", "[({(<(())[]>[[{[]{<()<>>"),
    ]
)
def test_first_corrupted_character(character: str, line: str):
    assert character == first_corrupted_character(line)


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 26397


def test_silver_star():
    assert silver(INPUT_PATH) == 323613
