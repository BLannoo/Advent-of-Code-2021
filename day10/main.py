from pathlib import Path

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "": 0,
}


def silver(input_file_path: Path) -> int:
    lines = input_file_path.read_text().split("\n")

    return sum(
        POINTS[
            first_corrupted_character(line)
        ]
        for line in lines
    )


BRACES = (
    "()",
    "[]",
    "{}",
    "<>",
)


def contains_consecutive_match(line: str) -> bool:
    for brace_pair in BRACES:
        if brace_pair in line:
            return True
    return False


def first_corrupted_character(line: str) -> str:
    while contains_consecutive_match(line):
        for brace_pair in BRACES:
            line = line.replace(brace_pair, "")

    first_closing = [
        line.find(brace_close)
        for _, brace_close in BRACES
        if brace_close in line
    ]

    if len(first_closing) == 0:
        return ""

    return line[min(first_closing)]
