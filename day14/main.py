from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict


@dataclass
class LinkedMonomers:
    value: str
    next_monomer: Optional["LinkedMonomers"]

    @staticmethod
    def from_str(polymer: str) -> "LinkedMonomers":
        if len(polymer) == 1:
            return LinkedMonomers(polymer[0], None)
        return LinkedMonomers(
            polymer[0],
            LinkedMonomers.from_str(polymer[1:])
        )


@dataclass
class Polymerizer:
    polymer: LinkedMonomers
    rules: Dict[str, str]

    @staticmethod
    def parse(input_file_path: Path) -> "Polymerizer":
        polymer, rules_str = input_file_path.read_text().split("\n\n")

        rules = {
            rule_str.split("->")[0].strip(): rule_str.split("->")[1].strip()
            for rule_str in rules_str.split("\n")
        }

        return Polymerizer(
            polymer=LinkedMonomers.from_str(polymer),
            rules=rules,
        )

    def polymerize_n_times(self, times: int) -> "Polymerizer":
        for _ in range(times):
            self.polymer = self.polymerize_once()
        return self

    def polymerize_once(self) -> "LinkedMonomers":
        cursor = self.polymer
        while cursor.next_monomer is not None:
            new_monomer = LinkedMonomers(
                value=self.rules[cursor.value + cursor.next_monomer.value],
                next_monomer=cursor.next_monomer,
            )
            cursor.next_monomer = new_monomer
            cursor = new_monomer.next_monomer

        return self.polymer

    def polymer_str(self):
        result = ""
        cursor = self.polymer
        while cursor is not None:
            result += cursor.value
            cursor = cursor.next_monomer
        return result

    def count(self) -> Dict[str, int]:
        return Counter(self.polymer_str())


def silver(input_file_path: Path) -> int:
    counts = Polymerizer.parse(input_file_path).polymerize_n_times(10).count()
    return max(counts.values()) - min(counts.values())
