from pathlib import Path

from day4.board import Board


def silver(input_file_path: Path) -> int:
    number_sequence, boards = parse_input(input_file_path)
    for number in number_sequence:
        for board in boards:
            board.mark(number)
            if board.is_won():
                return board.unmarked_sum() * number


def gold(input_file_path: Path) -> int:
    number_sequence, boards = parse_input(input_file_path)
    for number in number_sequence:
        for board in boards.copy():
            board.mark(number)
            if board.is_won():
                if len(boards) == 1:
                    return board.unmarked_sum() * number
                boards.remove(board)


def parse_input(input_file_path):
    split = input_file_path.read_text().split("\n\n")
    number_sequence = [
        int(number_str)
        for number_str in split[0].split(",")
    ]
    boards = [
        Board.parse(board_description)
        for board_description in split[1:]
    ]
    return number_sequence, boards
