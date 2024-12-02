############
# AoC 2023 #
##############################################
# https://adventofcode.com/2023/day/2        #  # TODO: Replace with the correct day number.
##############################################
# ...

# ALGORITHM
# 1. ...

# SOLUTIONS:
# ...

from typing import Literal

from utils import utils  # type: ignore

YEAR = 2023
DAY = 2  # TODO: Replace with the correct day number.
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
