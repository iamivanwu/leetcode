from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        last = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= last:
                last = i
        return last <= 0
nums = [1,2,3]
print(Solution().canJump(nums))