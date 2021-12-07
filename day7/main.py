from collections import Callable
from pathlib import Path
from typing import List


def silver(input_file_path: Path) -> int:
    return core(
        input_file_path,
        fuel_cost=lambda destination, initial_positions: len(initial_positions),
    )


def gold_fuel_cost(destination: int, initial_positions: List[int]) -> int:
    return sum(
        abs(initial_position - destination)
        for initial_position in initial_positions
    )


def gold(input_file_path: Path) -> int:
    return core(
        input_file_path,
        fuel_cost=gold_fuel_cost,
    )


def core(input_file_path: Path, fuel_cost: Callable[[int, List[int]], int]) -> int:
    positions = sorted([
        int(number)
        for number in input_file_path.read_text().split(",")
    ])

    front = positions.pop(-1)
    front_initial_positions = [front]
    back = positions.pop(0)
    back_initial_positions = [back]

    fuel = 0

    while front != back:
        while len(positions) > 0 and positions[-1] == front:
            front_initial_positions.append(positions.pop(-1))
        while len(positions) > 0 and positions[0] == back:
            back_initial_positions.append(positions.pop(0))
        fuel_cost_front = fuel_cost(front - 1, front_initial_positions)
        fuel_cost_back = fuel_cost(back + 1, back_initial_positions)
        if fuel_cost_back > fuel_cost_front:
            fuel += fuel_cost_front
            front -= 1
        else:
            fuel += fuel_cost_back
            back += 1

    return fuel
