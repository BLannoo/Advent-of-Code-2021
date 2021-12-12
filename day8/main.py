from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List

PATTERN_TO_DIGIT = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


@dataclass(frozen=True)
class Entry:
    raw: str

    @property
    def outputs(self) -> List[str]:
        return [
            ''.join(sorted(output))
            for output in self.raw.split(" | ")[1].split(" ")
        ]

    @property
    def patterns(self) -> List[str]:
        return [
            ''.join(sorted(pattern))
            for pattern in self.raw.split(" | ")[0].split(" ")
        ]

    def count_output_1478(self) -> int:
        return len(
            [
                output
                for output in self.outputs
                if len(output) in (2, 3, 4, 7)
            ]
        )

    def output_value(self) -> int:
        return int(
            "".join(
                [
                    self.decode(output)
                    for output in self.outputs
                ]
            )
        )

    def get_digit_pattern(self, digit: int) -> str:
        return {
            1: self._get_digit_pattern_by_length(2),
            4: self._get_digit_pattern_by_length(4),
            7: self._get_digit_pattern_by_length(3),
            8: self._get_digit_pattern_by_length(7),
        }[digit]

    def _get_digit_pattern_by_length(self, length: int) -> str:
        return [
            pattern
            for pattern in self.patterns
            if len(pattern) == length
        ][0]

    def get_actual_segment(self, displayed_segment):
        occurrences_map = {
            self._get_segments_by_occurrence(6)[0]: "b",
            self._get_segments_by_occurrence(4)[0]: "e",
            self._get_segments_by_occurrence(9)[0]: "f",
        }

        occurrence_8 = self._get_segments_by_occurrence(8)
        if occurrence_8[0] in self.get_digit_pattern(1):
            occurrence_8_map = {
                occurrence_8[0]: "c",
                occurrence_8[1]: "a",
            }
        else:
            occurrence_8_map = {
                occurrence_8[0]: "a",
                occurrence_8[1]: "c",
            }

        occurrence_7 = self._get_segments_by_occurrence(7)
        if occurrence_7[0] in self.get_digit_pattern(4):
            occurrence_7_map = {
                occurrence_7[0]: "d",
                occurrence_7[1]: "g",
            }
        else:
            occurrence_7_map = {
                occurrence_7[0]: "g",
                occurrence_7[1]: "d",
            }

        return {
            **occurrences_map,
            **occurrence_8_map,
            **occurrence_7_map,
        }.get(displayed_segment, "z")

    def _get_segments_by_occurrence(self, occurrence: int) -> List[str]:
        occurrences = Counter(self.raw.split(" | ")[0].replace(" ", ""))

        return [
            k
            for k, v in occurrences.items()
            if v == occurrence
        ]

    def decode(self, output: str) -> str:
        actual_pattern = "".join(
            sorted(
                [
                    self.get_actual_segment(displayed_segment)
                    for displayed_segment in output
                ]
            )
        )
        return PATTERN_TO_DIGIT[actual_pattern]


def silver(input_file_path: Path) -> int:
    return sum(
        [
            Entry(raw_entry).count_output_1478()
            for raw_entry in input_file_path.read_text().split("\n")
        ]
    )


def gold(input_file_path: Path) -> int:
    return sum(
        [
            Entry(raw_entry).output_value()
            for raw_entry in input_file_path.read_text().split("\n")
        ]
    )
