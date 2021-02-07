from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        rev = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                rev += 1
        if nums[0] < nums[-1]:
            rev += 1
        return False if rev > 1 else True