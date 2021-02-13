from typing import List


def romanToInt(s: str) -> int:
    total = 0
    symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    for index,char in enumerate(s):
        if index < len(s)-1 and symbol[s[index]] < symbol[s[index+1]]:
            total -= symbol[char]
        else:
            total += symbol[char]
    return total


class Solution:
    pass