from pathlib import Path

from day13.main import silver, gold

EXAMPLE_PATH = Path(__file__).parent / "example.txt"
INPUT_PATH = Path(__file__).parent / "input.txt"


def test_silver_example():
    assert silver(EXAMPLE_PATH) == 17


def test_silver_star():
    assert silver(INPUT_PATH) == 653


def test_gold_example():
    assert gold(EXAMPLE_PATH) == """
    #####
    #...#
    #...#
    #...#
    #####
    """.strip().replace(" ", "")


def test_gold_star():
    assert gold(INPUT_PATH) == """
    #....#..#.###..####.###..###..###..#..#
    #....#.#..#..#.#....#..#.#..#.#..#.#.#.
    #....##...#..#.###..###..#..#.#..#.##..
    #....#.#..###..#....#..#.###..###..#.#.
    #....#.#..#.#..#....#..#.#....#.#..#.#.
    ####.#..#.#..#.####.###..#....#..#.#..#
    """.strip().replace(" ", "")
