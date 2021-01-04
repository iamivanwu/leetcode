from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)*(len(nums)+1)//2
        for n in nums:
            res -= n
        return res