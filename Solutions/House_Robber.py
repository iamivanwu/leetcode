from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1],nums[0]+nums[2])
        f,s,t = nums[0], nums[1],nums[0]+nums[2]
        for i in range(3,len(nums)):
            temp = t
            t = nums[i] + max(f,s)
            f = s
            s = temp
        return max(s,t)
