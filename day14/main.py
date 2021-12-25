from pathlib import Path
from typing import Dict

import numpy as np

Monomer = str
Pair = str


def core(input_file_path: Path, times: int) -> float:
    counts = polymerize(input_file_path, times)
    return max(counts.values()) - min(counts.values())


def polymerize(input_file_path: Path, times: int) -> Dict[Monomer, float]:
    polymer_str, rules_str = input_file_path.read_text().split("\n\n")
    rules = parse_rules(rules_str)
    pairs_to_idx = {
        pair: idx
        for idx, pair in enumerate(rules.keys())
    }
    pair_count_vector = polymer_str_to_pair_count_vector(polymer_str, pairs_to_idx)
    transitions = transition_matrix(rules, pairs_to_idx)

    for _ in range(times):
        pair_count_vector = transitions.dot(pair_count_vector)

    return count_monomers(polymer_str, pairs_to_idx, pair_count_vector)


def parse_rules(rules_str: str) -> Dict[Pair, Monomer]:
    return {
        rule_str.split("->")[0].strip(): rule_str.split("->")[1].strip()
        for rule_str in rules_str.split("\n")
    }


def polymer_str_to_pair_count_vector(polymer_str: str, pairs_to_idx: Dict[Pair, int]) -> np.ndarray:
    polymer = np.zeros(len(pairs_to_idx))
    for prev_monomer, next_monomer in zip(polymer_str[:-1], polymer_str[1:]):
        polymer[pairs_to_idx[prev_monomer + next_monomer]] += 1
    return polymer


def transition_matrix(rules: Dict[Pair, Monomer], pairs_to_idx: Dict[Pair, int]) -> np.ndarray:
    transitions = np.zeros((len(pairs_to_idx),) * 2)
    for pair, insert in rules.items():
        transitions[pairs_to_idx[pair[0] + insert], pairs_to_idx[pair]] = 1
        transitions[pairs_to_idx[insert + pair[1]], pairs_to_idx[pair]] = 1
    return transitions


def count_monomers(
    polymer_str: str, pairs_to_idx: Dict[Pair, int], pair_count_vector: np.ndarray
) -> Dict[Monomer, float]:
    monomer_count = {}
    for monomer in (polymer_str[0], polymer_str[-1]):
        monomer_count[monomer] = monomer_count.get(monomer, 0) + 1 / 2
    for pair, idx in pairs_to_idx.items():
        for monomer in pair:
            monomer_count[monomer] = monomer_count.get(monomer, 0) + pair_count_vector[idx] / 2
    return monomer_count
