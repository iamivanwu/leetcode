from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        start,end = -1,-1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if start == -1:
                    start = end = i
                else:
                    end = i
        return end-start+1 if end-start else 0