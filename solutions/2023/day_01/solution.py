# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer


def replace_digits(digit: str) -> str:
    digits_to_replace = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for text, number in digits_to_replace.items():
        digit = digit.replace(text, f"{text}{number}{text}")

    return digit


def filter_digits(digit: str) -> bool:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if digit in digits:
        return True
    else:
        return False


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(54927)
    def part_1(self) -> int:
        total = 0
        for line in self.input:
            found_digits = list(filter(filter_digits, line))
            total += int(found_digits[0] + found_digits[-1])
        return total

    @answer(54581)
    def part_2(self) -> int:
        total = 0
        for line in self.input:
            replaced = replace_digits(line)
            found_digits = list(filter(filter_digits, replaced))
            total += int(found_digits[0] + found_digits[-1])
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
