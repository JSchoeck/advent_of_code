############
# AoC 2024 #
##############################################
# https://adventofcode.com/2024/day/1#part2  #
##############################################
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

# Here are the same example lists again:

# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# For these example lists, here is the process of finding the similarity score:

# The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
# The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
# The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
# The fourth number, 1, also does not appear in the right list.
# The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
# The last number, 3, appears in the right list three times; the similarity score again increases by 9.
# So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

# Once again consider your left and right lists. What is their similarity score?


# ALGORITHM
# 1. ...

# SOLUTIONS:
# ...

# %%
import sys
from pathlib import Path
from typing import Literal

import numpy as np

sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import utils

# %%
YEAR = 2024
DAY = 1
# MODE: Literal["Dev", "Test", "Solve"] = "Dev"
# MODE: Literal["Dev", "Test", "Solve"] = "Test"
MODE: Literal["Dev", "Test", "Solve"] = "Solve"

DEV_INPUT = [
    "",
]

# Official sample input:
TEST_INPUT = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]
TEST_SOLUTION = 31


def split_input_into_lists(input: list[str]) -> tuple[list[str], list[str]]:
    left_list, right_list = [], []
    for row in input:
        left, right = row.split()
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


def convert_lists(left: list[str], right: list[str]) -> tuple[list[str], list[str]]:
    left = list(map(int, left))  # type: ignore
    left = np.array(left)  # type: ignore
    right = list(map(int, right))  # type: ignore
    right = np.array(right)  # type: ignore
    return left, right


def value_count(item: int, values: list[int]) -> int:
    from collections import Counter

    counts = Counter(values)
    return counts[item]


def compute_similarity_score(input_values: list[str]) -> int:
    """Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list."""
    left, right = split_input_into_lists(input_values)
    left, right = convert_lists(left, right)
    similarity_sum = 0
    for i in left:
        similarity_sum += i * value_count(i, right)  # type: ignore
    return similarity_sum


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    utils.report_solution(MODE, TEST_SOLUTION, compute_similarity_score(input_values))


# %%
if __name__ == "__main__":
    main()
