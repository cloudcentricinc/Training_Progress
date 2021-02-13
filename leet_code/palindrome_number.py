from typing import List


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if str(x)[::-1] == str(x):
        return True
    return False


class Solution:
    pass
