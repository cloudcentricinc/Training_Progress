class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, element in enumerate(nums):
            if element >= target:
                return index
        return len(nums)