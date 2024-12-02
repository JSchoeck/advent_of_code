############
# AoC 2023 #
##############################################
# https://adventofcode.com/2023/day/3        #
##############################################
# any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.
# add up all the part numbers in the engine schematic, and report the sum.

# SOLUTION:
# ... --> ?

import contextlib
from typing import Literal

from utils import utils  # type: ignore

YEAR = 2023
DAY = 3
# MODE: Literal["Dev", "Test", "Solve"] = "Dev"
MODE: Literal["Dev", "Test", "Solve"] = "Test"
# MODE: Literal["Dev", "Test", "Solve"] = "Solve"

DEV_INPUT = [
    "",
]

# Official sample input:
TEST_INPUT = [
    "467..114..",  # 114 not valid
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",  # 58 not valid
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]
TEST_SOLUTION = 4361

SPECIAL_CHARS = set()


def find_chars_in_current_row(row: str) -> list[int]:
    indices = []
    not_special_chars = {str(_) for _ in list(range(0, 10))}
    not_special_chars.add(".")
    for i, char in enumerate(row):
        if char not in not_special_chars:
            SPECIAL_CHARS.add(char)
        if char in SPECIAL_CHARS:
            indices.append(i)
    return indices


def remove_special_chars(value: str) -> str:
    for char in SPECIAL_CHARS:
        value = value.replace(char, "")
    return value


def find_numbers_in_current_row(row: str) -> list[range]:
    """Finds numbers in a row and returns their starting position and length.

    Args:
        row (str): raw row string.

    Returns:
        list[range]: list of all starting positions and lengths of numbers in the row.
    """
    row_no_special_chars = remove_special_chars(row)
    numbers = row_no_special_chars.split(".")
    numbers_cleaned = []
    for number in numbers:
        if number == "":
            continue
        numbers_cleaned.append(number)
    ranges = []
    for number in numbers_cleaned:
        ranges.append(range(row.find(number), len(number)))
    # TODO: change to dict with actual number as key?
    return ranges


def analyze_row(
    pos_of_chars_row_current: list[int], pos_of_chars_row_previous: list[int], numbers: list[range]
) -> tuple[int, bool]:
    line_sum = 0
    for number in numbers:
        if pos_of_chars_row_current in number:
            line_sum += int(number)
    print(pos_of_chars_row_current)
    print(pos_of_chars_row_previous)
    print(numbers)
    return 1, True


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    solution = 0
    part_no_sums = {}
    pos_of_chars_row_previous = []
    pos_of_chars_row_current = []
    for i, row_raw in enumerate(input_values):
        row = row_raw.strip()
        pos_of_chars_row_current = find_chars_in_current_row(row)
        numbers = find_numbers_in_current_row(row)
        part_no_sum, result = analyze_row(pos_of_chars_row_current, pos_of_chars_row_previous, numbers)
        part_no_sums[i] = part_no_sum
        if result:
            solution += part_no_sum
        pos_of_chars_row_previous = pos_of_chars_row_current

    # utils.report_solution(MODE, TEST_SOLUTION, solution)
    print("\nSolutions per row:")
    [print(row_no, "->", part_no_sum) for row_no, part_no_sum in part_no_sums.items()]
    # print(SPECIAL_CHARS)


if __name__ == "__main__":
    main()
