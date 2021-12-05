from pathlib import Path
from typing import List, Callable


def silver(input_file_path: Path) -> int:
    diagnostic_report = input_file_path.read_text().split("\n")

    gamma_rate = silver_rate(diagnostic_report, least_common_bit)
    epsilon_rate = silver_rate(diagnostic_report, most_common_bit)

    return gamma_rate * epsilon_rate


def gold(input_file_path: Path) -> int:
    diagnostic_report = input_file_path.read_text().split("\n")

    oxygen_generator_rating = gold_rate(diagnostic_report, most_common_bit)
    co2_scrubber_rating = gold_rate(diagnostic_report, least_common_bit)

    return oxygen_generator_rating * co2_scrubber_rating


def silver_rate(
    diagnostic_report: List[str],
    bit_selector: Callable[[List[str], int], int]
) -> int:
    bits = [
        bit_selector(diagnostic_report, i)
        for i in range(len(diagnostic_report[0]))
    ]
    return binary_to_int(bits)


def gold_rate(
    diagnostic_report: List[str],
    bit_selector: Callable[[List[str], int], int]
) -> int:
    for i in range(len(diagnostic_report)):

        if len(diagnostic_report) == 1:
            return int(diagnostic_report[0], 2)

        diagnostic_report = list(filter(
            lambda binary: int(binary[i]) == bit_selector(diagnostic_report, i),
            diagnostic_report
        ))


def most_common_bit(diagnostic_report: List[str], at: int) -> int:
    return (least_common_bit(diagnostic_report, at) + 1) % 2


def least_common_bit(diagnostic_report: List[str], at: int) -> int:
    bits = [
        int(binary_number[at])
        for binary_number in diagnostic_report
    ]

    ones = sum(bits)
    zeros = len(diagnostic_report) - ones

    return int(ones < zeros)


def binary_to_int(least_common_bits: List[int]) -> int:
    return int(
        "".join(
            [
                str(bit)
                for bit in least_common_bits
            ]
        ),
        base=2,
    )
