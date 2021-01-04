from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = [0 for i in range(len(nums))]
        for n in nums:
            if a[n]:
                return n
            else:
                a[n] = 1