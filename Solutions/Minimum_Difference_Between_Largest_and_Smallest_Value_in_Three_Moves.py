from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[3:][-1]-nums[3:][0],nums[2:-1][-1]-nums[2:-1][0],nums[1:-2][-1]-nums[1:-2][0],nums[0:-3][-1]-nums[0:-3][0])
nums = [1,5,0,10,14]
print(Solution().minDifference(nums))