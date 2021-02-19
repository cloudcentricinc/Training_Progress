from typing import List


def removeElement(nums: List[int], val: int) -> int:
    loc = 0
    for index in range(len(nums)):
        if nums[index] != val:
            nums[loc] = nums[index]
            loc += 1
    return loc


class Solution:
    pass