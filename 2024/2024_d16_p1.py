############
# AoC 2024 #
##############################################
# https://adventofcode.com/2024/day/16       #
##############################################
# What is the lowest score a Reindeer could possibly get?

# ALGORITHM
# 1. ...

# SOLUTION:
#

import sys
from pathlib import Path
from typing import Any, Literal

import numpy as np

# Add the parent directory to the sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import utils

YEAR = 2024
DAY = 16
MODE: Literal["Test", "Solve"] = "Test"
# MODE: Literal["Test", "Solve"] = "Solve"

COST_STEP = 1
COST_TURN = 1000
WALL = "#"
END = "E"
START = "S"
START_DIR = enumerate(["East", "South", "West", "North"])

# Official sample input:
TEST_INPUT = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()
TEST_SOLUTION = 7036
TEST_INPUT2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()
TEST_SOLUTION2 = 11048


def calculate_answer(input_values: list[str]) -> int:
    return -1


def init_grid(grid_string: list[str]) -> np.ndarray:
    grid = [list(row) for row in grid_string]
    return np.array(grid)


def get_start(grid: np.ndarray) -> tuple[int, int]:
    return tuple(np.argwhere(grid == START).flatten())


def get_end(grid: np.ndarray) -> tuple[int, int]:
    return tuple(np.argwhere(grid == END).flatten())


def dijkstra(
    grid: np.ndarray, start: tuple[int, int], cost_step: int = 1, cost_turn: int = 1000
) -> tuple[dict[Any, Any], dict[Any, Any]]:
    dist = {}
    prev = {}
    q = []
    facing_horizontal = True
    for index in np.ndindex(grid.shape):
        if grid[index] != WALL:
            dist[index] = np.inf
            prev[index] = None
            q.append(index)
    dist[start] = 0

    u = (0, 0)
    turn_needed = False
    while len(q) > 0:
        min_dist = np.inf
        for v in q:
            if dist[v] < min_dist:
                if turn_needed:
                    facing_horizontal = not facing_horizontal
                min_dist = dist[v]
                u = v
        if u in q:
            q.remove(u)
        unvisited_neighbors = [(u[0], u[1] + 1), (u[0], u[1] - 1), (u[0] + 1, u[1]), (u[0] - 1, u[1])]
        available_neighbors = [a for a in unvisited_neighbors if a in q]
        for n in available_neighbors:
            cost = cost_step
            # BUG: not yet correctly taking into account where we are coming from
            if (facing_horizontal and (u[0] != n[0])) or (not facing_horizontal and (u[1] != n[1])):
                print(f"Turning from {u=} to {n=} ({facing_horizontal=})")
                cost += cost_turn
                turn_needed = True
            alt = dist[u] + cost
            print(f"Cost for {u=}->{n=}: {cost} (total {alt=})")
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
        # print(u)
    return dist, prev


def main() -> None:
    match MODE:
        case "Test":
            input_values = TEST_INPUT
        case "Solve":
            input_values = utils.load_input(YEAR, DAY)

    grid = init_grid(input_values)  # type: ignore
    # print(grid.shape)
    start = get_start(grid)
    end = get_end(grid)
    dist, prev = dijkstra(grid, start)
    current = prev[end]
    grid_solved = grid.copy()
    while (d := dist[current]) > 0:
        last = prev[current]
        grid_solved[current[0]][current[1]] = "^"
        # print(f"{d=}, {current=}, {last=}")
        current = last
    # print("\n".join(TEST_INPUT2))
    print(np.array2string(grid_solved, separator="").replace("'", "").replace("[", "").replace("]", ""))
    print("Distance S->E", dist[end])

    utils.report_solution(MODE, TEST_SOLUTION, dist[end])


if __name__ == "__main__":
    main()
