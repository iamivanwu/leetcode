from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        res = 1
        d = 1 if nums[1] < nums[0] else -1 if nums[1] > nums[0] else 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 0:
                if d == -1 or d == 0:
                    res += 1
                d = 1 
            elif nums[i] - nums[i-1] < 0:
                if d == 1 or d == 0:
                    res += 1
                d = -1
            print(res,nums[i])
        return res
nums = [3,3,3,2,5]
print(Solution().wiggleMaxLength(nums))
