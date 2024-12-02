############
# AoC 2023 #
##############################################
# https://adventofcode.com/2023/day/1#part2  #
##############################################
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# ALGORITHM
# 1. Read the input values from a file or use example input.
# 2. Loop over each line.
# 3. For each line, find the first digit and the last digits.
#    - If the first digit is spelled out, return the digit.
#    - If the last digit is spelled out, return the digit.
#    - If the first digit is a number, return the digit.
#    - If the last digit is a number, return the digit.
# 4. Combine the two digits to form a two-digit number.
# 5. Sum all the two-digit numbers.
# 6. Print the total sum.

# SOLUTIONS:
# 53810 is too low; # TODO what edge case am I missing?

from typing import Literal

from utils import utils  # type: ignore

YEAR = 2023
DAY = 1
# MODE: Literal["Dev", "Test", "Solve"] = "Dev"
# MODE: Literal["Dev", "Test", "Solve"] = "Test"
MODE: Literal["Dev", "Test", "Solve"] = "Solve"

DEV_INPUT = [
    "abconethreexyz",
    "1asd2sdfg3",
    "4",
]

# Official sample input:
TEST_INPUT = [
    "two1nine",  # 29
    "eightwothree",  # 83
    "abcone2threexyz",  # 13
    "xtwone3four",  # 24
    "4nineeightseven2",  # 42
    "zoneight234",  # 14
    "7pqrstsixteen",  # 76
]
TEST_SOLUTION = 281

SPELLED_OUT_DIGITS = {
    # "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    total_calibration_value = sum_calibration_values(input_values)

    utils.report_solution(MODE, TEST_SOLUTION, total_calibration_value)


def find_calibration_value(line: str) -> int:
    """Scan the line for the first and last digit, either as a spelled-out word or a number.

    Args:
        line (str): text input

    Returns:
        int: two-digit number formed by the first and last digit
    """
    # print(line)
    first_digit = get_first_digit(line)
    # print(first_digit)
    last_digit = get_last_digit(line)
    # print(last_digit)
    calibration_value = int(str(first_digit) + str(last_digit))
    print(line, "-->", calibration_value)
    return calibration_value


def get_first_digit(line: str) -> str | None:
    for i in range(len(line)):
        for j in range(i, i + 3):
            if line[j].isdigit():
                return line[j]
        for digit in SPELLED_OUT_DIGITS:
            if digit in line[i : i + 3]:
                return SPELLED_OUT_DIGITS[digit]
        for digit in SPELLED_OUT_DIGITS:
            if digit in line[i : i + 5]:
                return SPELLED_OUT_DIGITS[digit]
    return "0"


def get_last_digit(line: str) -> str | None:
    for i in range(len(line), 0, -1):
        if line[i - 1].isdigit():
            return line[i - 1]
        for digit in SPELLED_OUT_DIGITS:
            if digit in line[i - 3 : i]:
                return SPELLED_OUT_DIGITS[digit]
        for digit in SPELLED_OUT_DIGITS:
            if digit in line[i - 4 : i]:
                return SPELLED_OUT_DIGITS[digit]
        for digit in SPELLED_OUT_DIGITS:
            if digit in line[i - 5 : i]:
                return SPELLED_OUT_DIGITS[digit]
    return "0"


def sum_calibration_values(input_values: list[str]) -> int:
    total_calibration_value = 0
    for line in input_values:
        total_calibration_value += find_calibration_value(line)
    return total_calibration_value


if __name__ == "__main__":
    main()
