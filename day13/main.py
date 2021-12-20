import re
from dataclasses import dataclass
from pathlib import Path
from typing import Set, Tuple, List


@dataclass(frozen=True)
class Instruction:
    dir: str
    loc: int

    @staticmethod
    def parse(desc: str) -> "Instruction":
        match = re.match(r"^fold along (?P<dir>x|y)=(?P<loc>\d+)$", desc)
        return Instruction(dir=match.group("dir"), loc=int(match.group("loc")))


@dataclass(frozen=True)
class Dot:
    x: int
    y: int

    def fold(self, instruction: Instruction) -> "Dot":
        if instruction.dir == "x":
            if instruction.loc < self.x:
                return Dot(2 * instruction.loc - self.x, self.y)
            elif instruction.loc > self.x:
                return self
            else:
                raise Exception(f"{self=} lies on fold {instruction=}")
        elif instruction.dir == "y":
            if instruction.loc < self.y:
                return Dot(self.x, 2 * instruction.loc - self.y)
            elif instruction.loc > self.y:
                return self
            else:
                raise Exception(f"{self=} lies on fold {instruction=}")
        else:
            raise Exception(f"Invalid instruction not x or y {instruction=}")


def silver(input_file_path: Path) -> int:
    dots, instructions = parse_input(input_file_path)

    dots = {
        dot.fold(instructions[0])
        for dot in dots
    }

    return len(dots)


def gold(input_file_path: Path) -> str:
    dots, instructions = parse_input(input_file_path)

    for instruction in instructions:
        dots = {
            dot.fold(instruction)
            for dot in dots
        }

    x_max = max(dot.x for dot in dots)
    y_max = max(dot.y for dot in dots)

    representation = "\n".join(
        "".join(
            "#" if Dot(x, y) in dots else "."
            for x in range(x_max + 1)
        )
        for y in range(y_max + 1)
    )

    return representation


def parse_input(input_file_path: Path) -> Tuple[Set[Dot], List[Instruction]]:
    dots_desc, instructions_desc = input_file_path.read_text().split("\n\n")
    dots = {
        Dot(*(int(cord) for cord in dot.split(",")))
        for dot in dots_desc.split("\n")
    }
    instructions = [
        Instruction.parse(instruction_desc)
        for instruction_desc in instructions_desc.split("\n")
    ]
    return dots, instructions
