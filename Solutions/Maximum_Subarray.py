from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        last = nums[0]
        m = nums[0]
        for num in nums[1:]:
            if last < 0 and num > 0:
                last = num
            elif last + num > 0:
                last += num
            else:
                last = num
            if last > m:
                m = last
        return m
nums = [1]
print(Solution().maxSubArray(nums))
