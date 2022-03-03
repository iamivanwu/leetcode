from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp,res = 0,0
        if len(nums) < 3:
            return 0
        d = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == d:
                dp += 1
                res += dp
            else:
                dp = 0
            d = nums[i] - nums[i-1]
        return res
print(Solution().numberOfArithmeticSlices([1,2,3,4,5,6]))