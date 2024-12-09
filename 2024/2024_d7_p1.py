############
# AoC 2024 #
##############################################
# https://adventofcode.com/2024/day/7        #
##############################################
# which test values could possibly be produced by placing any combination of operators into their calibration equations
# Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.
# Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged.
# Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).
# The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true.
# What is their total calibration result?

# ALGORITHM
# 1. Split line at colon into test value and equation values.
# 2. Loop while check if equation equals test value not true
# 1. Set all operator positions to +
# 2. Set "next" operator to *
# 3. If loop stops due to true, add to solution sum


# SOLUTION:
# 267566105056 -> OK

import sys
from itertools import product
from pathlib import Path
from typing import Literal

# Add the parent directory to the sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import utils

YEAR = 2024
DAY = 7
MODE: Literal["Test", "Solve"] = "Test"
# MODE: Literal["Test", "Solve"] = "Solve"


# Official sample input:
TEST_INPUT = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]
TEST_SOLUTION = 3749


def is_possible(test_value: int, numbers: list[int]) -> int:
    for operators in product((True, False), repeat=len(numbers) - 1):
        result = numbers[0]
        # for number, operator in zip(numbers[1:], operators, strict=True):
        #     result = result + number if operator else result * number
        for pos, operator in enumerate(operators, start=1):
            match operator:
                case True:
                    result += numbers[pos]
                case False:
                    result *= numbers[pos]
        if result == test_value:
            return test_value
    return 0


def calculate_value(lines: list[str]) -> int:
    result = 0
    for line in lines:
        test_value, rest = line.split(": ")
        test_value = int(test_value)
        numbers = [int(i) for i in rest.split()]
        result += is_possible(test_value, numbers)
    return result


def load_input(year: int, day: int) -> list:
    with open(f"C:/users/moritz.ratzesberger/Downloads/{year}_d{day}.txt") as f:
        actual_input = f.readlines()
    return actual_input


def main() -> None:
    match MODE:
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    utils.report_solution(MODE, TEST_SOLUTION, calculate_value(input_values))


if __name__ == "__main__":
    main()
