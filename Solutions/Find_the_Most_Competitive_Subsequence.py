from typing import List
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            while res and res[-1] > nums[i] and len(nums)-i-1 >= k-len(res):
                res.pop()
            if len(res) < k:
                res.append(nums[i])
        return res