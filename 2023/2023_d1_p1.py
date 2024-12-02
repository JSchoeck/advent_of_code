############
# AoC 2023 #
########################################
# https://adventofcode.com/2023/day/1  #
########################################

TESTING = False


def d1_p1() -> None:
    # On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
    d1_example_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    # In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

    with open("2023_d1.txt") as f:
        actual_input = f.readlines()

    input_values = d1_example_input if TESTING else actual_input

    total_calibration_value = 0
    for line in input_values:
        total_calibration_value += find_calibration_value(line)
    print(f"{total_calibration_value=}")


def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char
    msg = f"No digit found in {line=}"
    raise ValueError(msg)


def find_calibration_value(line: str) -> int:
    first_digit = get_first_digit(line)
    # get last digit by inverting the line and getting the first digit
    last_digit = get_first_digit(line[::-1])
    return int(first_digit + last_digit)


if __name__ == "__main__":
    d1_p1()
