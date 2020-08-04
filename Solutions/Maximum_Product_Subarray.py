from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pos = neg = m = nums[0]
        for i in range(1,len(nums)):
            pos_n = max(pos*nums[i],neg*nums[i],nums[i])
            neg_n = min(pos*nums[i],neg*nums[i],nums[i])
            m = max(pos_n,neg_n,m)
            pos = pos_n
            neg = neg_n
        return m
nums = [1,0,-1,2,3,-5,-2]
nums = [2,3,-2,4]
print(Solution().maxProduct(nums))
