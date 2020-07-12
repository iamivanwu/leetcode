from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        count = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count