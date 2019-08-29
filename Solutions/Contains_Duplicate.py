from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums.sort()
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp == nums[i]:
                return True
            temp = nums[i]
        return False

nums = [1,2,3,1]
nums = []
sol = Solution()
print(sol.containsDuplicate(nums))