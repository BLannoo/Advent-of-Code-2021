from pathlib import Path
from typing import List


def silver(input_file_path: Path) -> int:
    diagnostic_report = input_file_path.read_text().split("\n")

    gamma_rate = rate(diagnostic_report, least_common_bit)
    epsilon_rate = rate(diagnostic_report, most_common_bit)

    return gamma_rate * epsilon_rate


def rate(diagnostic_report, bit_selector):
    bits = [
        bit_selector(diagnostic_report, at=i)
        for i in range(len(diagnostic_report[0]))
    ]
    return binary_to_int(bits)


def most_common_bit(diagnostic_report: List[str], at: int) -> int:
    return (least_common_bit(diagnostic_report, at) + 1) % 2


def least_common_bit(diagnostic_report: List[str], at: int) -> int:
    bits = [
        int(binary_number[at])
        for binary_number in diagnostic_report
    ]

    return len(diagnostic_report) // sum(bits) - 1


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
