from day4.board import Board

EXAMPLE_BOARD_1 = """
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19
""".strip("\n")


def test_win_first_row():
    board = Board.parse(EXAMPLE_BOARD_1)
    for number in [22, 13, 17, 11, 0]:
        assert not board.is_won()
        board.mark(number)
    assert board.is_won()


def test_win_last_row():
    board = Board.parse(EXAMPLE_BOARD_1)
    for number in [1, 12, 20, 15, 19]:
        assert not board.is_won()
        board.mark(number)
    assert board.is_won()


def test_win_first_column():
    board = Board.parse(EXAMPLE_BOARD_1)
    for number in [22, 8, 21, 6, 1]:
        assert not board.is_won()
        board.mark(number)
    assert board.is_won()


def test_win_last_column():
    board = Board.parse(EXAMPLE_BOARD_1)
    for number in [0, 24, 7, 5, 19]:
        assert not board.is_won()
        board.mark(number)
    assert board.is_won()


EXAMPLE_BOARD_2 = """
14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".strip("\n")


def test_unmarked_sum():
    board = Board.parse(EXAMPLE_BOARD_2)
    for number in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
        assert not board.is_won()
        board.mark(number)
    assert board.is_won()
    assert board.unmarked_sum() == 188
