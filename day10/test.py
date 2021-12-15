from pathlib import Path

import pytest

from day10.main import silver, first_corrupted_character, gold, find_completion, completion_scoring

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


@pytest.mark.parametrize(
    "line,completion",
    [
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
    ]
)
def test_completion(line: str, completion: str):
    assert find_completion(line) == completion


@pytest.mark.parametrize(
    "completion,score",
    [
        ("}}]])})]", 288957),
        (")}>]})", 5566),
        ("}}>}>))))", 1480781),
        ("]]}}]}]}>", 995444),
        ("])}>", 294),
    ]
)
def test_completion_scoring(completion: str, score: int):
    assert completion_scoring(completion) == score


def test_gold_example():
    assert gold(EXAMPLE_PATH) == 288957


def test_gold_star():
    assert gold(INPUT_PATH) == 3103006161
