from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Entry:
    raw: str

    @property
    def outputs(self):
        return self.raw.split(" | ")[1].split(" ")

    def count_output_1478(self):
        return len(
            [
                output
                for output in self.outputs
                if len(output) in (2, 3, 4, 7)
            ]
        )


def silver(input_file_path: Path) -> int:
    return sum(
        [
            Entry(raw_entry).count_output_1478()
            for raw_entry in input_file_path.read_text().split("\n")
        ]
    )
