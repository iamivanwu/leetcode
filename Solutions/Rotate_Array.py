from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(k):
            temp.append(nums[(i-k)%len(nums)])
        for i in range(len(nums)):
            temp.append(nums[i])
            nums[i] = temp.pop(0)

nums = [-1,2,3]
k = 5
Solution().rotate(nums,k)
print(nums)