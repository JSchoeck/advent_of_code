import logging
from typing import Literal

logging.basicConfig(level=logging.INFO, format="%(message)s")


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
DEFAULT = "\033[0m"


def load_input(year: int, day: int) -> list:
    with open(f"./{year}/inputs/{year}_d{day}.txt") as f:
        actual_input = f.readlines()
    logging.info(f"Read input of length: {len(actual_input)}")
    return actual_input


def report_solution(mode: Literal["Dev", "Test", "Solve"], example_solution: int, solution: int) -> None:
    match mode:
        case "Dev":
            print(f"\n{BLUE}Theoretical solution:{DEFAULT} {solution}")
        case "Test":
            print(f"\n{BLUE}Example solution:{DEFAULT} {example_solution}\
              \n{BLUE}My solution:{DEFAULT} {solution}")
            try:
                assert solution == example_solution
                print(f"\n{GREEN}Test passed!{DEFAULT}")
            except AssertionError:
                print(f"\n{RED}Test failed!{DEFAULT} {solution} != {example_solution}")
        case "Solve":
            print(f"\n{BLUE}Solution:{DEFAULT}\n{solution}")
