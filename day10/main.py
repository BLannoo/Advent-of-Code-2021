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


def gold(input_file_path: Path) -> int:
    lines = input_file_path.read_text().split("\n")

    completion_scores = [
        completion_scoring(find_completion(line))
        for line in lines
        if first_corrupted_character(line) == ""
    ]

    completion_scores.sort()

    middle_index = int((len(completion_scores)) / 2)

    return completion_scores[middle_index]


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
    line = remove_matching(line)

    first_closing = [
        line.find(brace_close)
        for _, brace_close in BRACES
        if brace_close in line
    ]

    if len(first_closing) == 0:
        return ""

    return line[min(first_closing)]


def remove_matching(line):
    while contains_consecutive_match(line):
        for brace_pair in BRACES:
            line = line.replace(brace_pair, "")
    return line


def close(brace: str) -> str:
    for brace_open, brace_close in BRACES:
        if brace == brace_open:
            return brace_close
    raise Exception(f"brace '{brace}' not matched")


def find_completion(line: str) -> str:
    line = remove_matching(line)
    return "".join(
        close(brace)
        for brace in line[::-1]
    )


COMPLETION_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def completion_scoring(completion: str) -> int:
    score = 0
    for brace in completion:
        score *= 5
        score += COMPLETION_POINTS[brace]
    return score
