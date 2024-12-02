############
# AoC 2024 #
##############################################
# https://adventofcode.com/2024/day/1        #  # TODO: Replace with the correct day number.
##############################################
# ...

# ALGORITHM
# 1. ...

# SOLUTIONS:
# ...

import sys
from pathlib import Path
from typing import Literal

# Add the parent directory to the sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import utils

YEAR = 2024
DAY = 1  # TODO: Replace with the correct day number.
# MODE: Literal["Dev", "Test", "Solve"] = "Dev"
MODE: Literal["Dev", "Test", "Solve"] = "Test"
# MODE: Literal["Dev", "Test", "Solve"] = "Solve"

DEV_INPUT = [
    "",
]

# Official sample input:
TEST_INPUT = [  # TODO: Replace with the test input.
    "",
]
TEST_SOLUTION = -1  # TODO: Replace with the solution for the test input.


def do_something() -> None:
    return


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    utils.report_solution(MODE, TEST_SOLUTION, do_something)


if __name__ == "__main__":
    main()
