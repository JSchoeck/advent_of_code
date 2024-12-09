############
# AoC 2024 #
##############################################
# https://adventofcode.com/2024/day/1        #  # TODO: Replace with the correct day number.
##############################################
# ...

# ALGORITHM
# 1. ...

# SOLUTION:
#

import sys
from pathlib import Path
from typing import Literal

# Add the parent directory to the sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import utils

YEAR = 2024
DAY = 1  # TODO: Replace with the correct day number.
MODE: Literal["Test", "Solve"] = "Test"
# MODE: Literal["Test", "Solve"] = "Solve"


# Official sample input:
TEST_INPUT = [  # TODO: Replace with the test input.
    "",
]
TEST_SOLUTION = -1  # TODO: Replace with the solution for the test input.


def calculate_answer(input_values: str) -> None:
    return


def main() -> None:
    match MODE:
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    utils.report_solution(MODE, TEST_SOLUTION, calculate_answer(input_values))


if __name__ == "__main__":
    main()
