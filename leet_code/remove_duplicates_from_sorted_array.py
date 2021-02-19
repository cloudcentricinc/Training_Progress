from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if nums is None:
        return 0
    if len(nums) == 1:
        return 1
    loc = 0
    for index in range(1, len(nums)):
        if nums[loc] != nums[index]:
            loc += 1
            nums[loc] = nums[index]
    return loc + 1


class Solution:
    pass
