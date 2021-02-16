class Solution(object):
   def twoSum(self, arr, target):
    length = len(arr)
    for i in range(length - 1):
        for j in range(1, length):
            # print(i, j)
            if arr[i] + arr[j] == target:
                return i, j
    return None
input_list = [2,7,11,15]
ob1 = Solution()
print("result")
print(ob1.twoSum(input_list, 9))
