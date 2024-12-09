############
# AoC 2024 #
##############################################
# https://adventofcode.com/2024/day/1        #
##############################################
# There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

# For example:

# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

# In the example list above, the pairs and distances would be as follows:

# The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
# The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
# The third-smallest number in both lists is 3, so the distance between them is 0.
# The next numbers to pair up are 3 and 4, a distance of 1.
# The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
# Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

# Your actual left and right lists contain many location IDs. What is the total distance between your lists?


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
TEST_SOLUTION = 11


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


def find_differences(input_values: list[str]) -> int:
    left, right = split_input_into_lists(input_values)
    left, right = convert_lists(left, right)
    sum_diffs = 0
    left.sort()
    right.sort()
    sum_diffs = (abs(left - right)).sum()  # type: ignore
    return sum_diffs


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    utils.report_solution(MODE, TEST_SOLUTION, find_differences(input_values))


# %%
if __name__ == "__main__":
    main()
