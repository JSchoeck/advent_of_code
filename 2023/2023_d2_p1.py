############
# AoC 2023 #
##############################################
# https://adventofcode.com/2023/day/2        #
##############################################
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

# SOLUTION:
# 2369 --> correct

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
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",  # possible
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",  # possible
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",  # not possible
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",  # not possible
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",  # possible
]
TEST_SOLUTION = 8

BAG_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
BAG_LIMITS["total"] = sum(BAG_LIMITS.values())


def get_pieces(bag_content: list[str]) -> dict[str, int]:
    pieces = {}
    for i in range(0, len(bag_content)):
        shown = bag_content[i].split(", ")
        pieces.update({s.split(" ")[1]: int(s.split(" ")[0]) for s in shown})
    return pieces


def check_draw_rules(game_id: int, pieces: dict[str, int]) -> bool:
    for color, count in pieces.items():
        # Too many pieces of a single color
        if count > BAG_LIMITS[color]:
            print(f"Game {game_id} not possible, {count} {color} > bag limit of {BAG_LIMITS[color]}")
            return False

    # Too many total pieces
    total_pieces = sum(pieces.values())
    if total_pieces > BAG_LIMITS["total"]:
        print(f'Game {game_id} not possible, {total_pieces} > bag limit of {BAG_LIMITS["total"]}')
        return False

    # If no rule was violated, game is possible
    return True


def check_game_possibility(game: str) -> tuple[int, bool]:
    game_id, bag_content = game.split(": ")
    game_id = int(game_id.split(" ")[1])
    for i, draw in enumerate(bag_content.split("; ")):
        # print("ID", game_id, "Draw", i, "->", draw)
        pieces = get_pieces(draw.split(", "))
        result = check_draw_rules(game_id, pieces)
        if not result:
            return (game_id, False)
    return (game_id, True)


def main() -> None:
    match MODE:
        case "Dev":
            input_values = DEV_INPUT
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    solution = 0
    possible_games = {}
    for game in input_values:
        game_id, result = check_game_possibility(game.strip())
        if result:
            solution += game_id
            possible_games[game_id] = game

    utils.report_solution(MODE, TEST_SOLUTION, solution)
    print("\nPossible games:")
    [print(game, end="") for game_id, game in possible_games.items()]


if __name__ == "__main__":
    main()
