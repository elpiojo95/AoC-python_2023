# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

import re

from ...base import StrSplitSolution, answer

ELF_CUBES = {"red": 12, "green": 13, "blue": 14}


def get_game_id(set: str) -> int:
    return int(re.search(r"Game (\b\d+).", set).group(1))

def get_sets(game: str) -> str:
    return game.split(":")[1].split(";")

def get_cubes(set: str, color: str) -> int:
    result = re.search(r"(\b\d+)." + color, set)
    return int(result.group(1)) if result else 0

def is_set_valid(set: str) -> bool:
    if get_cubes(set, "blue") > ELF_CUBES["blue"]:
        return False
    if get_cubes(set, "red") > ELF_CUBES["red"]:
        return False
    if get_cubes(set, "green") > ELF_CUBES["green"]:
        return False
    return True

def is_game_valid(game: str) -> bool:
    for set in get_sets(game):
        if not is_set_valid(set):
            return False
    return True

def game_power(game: str) -> int:
    blue = red = green = 0
    for set in get_sets(game):
        blue = max(get_cubes(set, 'blue'), blue)
        red = max(get_cubes(set, 'red'), red)
        green = max(get_cubes(set, 'green'), green)
    return blue * red * green


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2169)
    def part_1(self) -> int:
        total = 0
        for game in self.input:
            game_id = get_game_id(game)
            if is_game_valid(game):
                total += game_id

        return total

    @answer(60948)
    def part_2(self) -> int:
        total = 0
        for game in self.input:
            total += game_power(game)

        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
