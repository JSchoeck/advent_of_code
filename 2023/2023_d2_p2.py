############
# AoC 2023 #
##############################################
# https://adventofcode.com/2023/day/2#part2  #
##############################################
# what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

# SOLUTIONS:
# 66363 --> correct

import math
from typing import Literal

from utils import utils  # type: ignore

YEAR = 2023
DAY = 2
# MODE: Literal["Dev", "Test", "Solve"] = "Dev"
# MODE: Literal["Dev", "Test", "Solve"] = "Test"
MODE: Literal["Dev", "Test", "Solve"] = "Solve"

DEV_INPUT = [
    "",
]

# Official sample input:
TEST_INPUT = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",  # 48
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",  # 12
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",  # 1560
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",  # 630
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",  # 36
]
TEST_SOLUTION = 2286

BAG_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def calculate_game_power(min_pieces: dict[str, int]) -> int:
    return int(math.prod(min_pieces.values()))


def update_min_pieces(min_pieces: dict[str, int], pieces: dict[str, int]) -> dict[str, int]:
    for color in pieces:
        min_pieces[color] = pieces[color] if pieces[color] > min_pieces[color] else min_pieces[color]
    return min_pieces


def get_pieces(bag_content: list[str]) -> dict[str, int]:
    pieces = {}
    for i in range(0, len(bag_content)):
        shown = bag_content[i].split(", ")
        pieces.update({s.split(" ")[1]: int(s.split(" ")[0]) for s in shown})
    return pieces


def get_game_power(game: str) -> tuple[int, int]:
    game_id, bag_content = game.split(": ")
    game_id = int(game_id.split(" ")[1])
    min_pieces = {color: 0 for color in BAG_LIMITS}
    for draw in bag_content.split("; "):
        # print("ID", game_id, "Draw", i, "->", draw)
        pieces = get_pieces(draw.split(", "))
        min_pieces = update_min_pieces(min_pieces, pieces)
    power = calculate_game_power(min_pieces)
    # print("ID", game_id, "Power", power)
    return (game_id, power)


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    solution = 0
    for game in input_values:
        game_id, result = get_game_power(game.strip())
        solution += result

    utils.report_solution(MODE, TEST_SOLUTION, solution)


if __name__ == "__main__":
    main()
