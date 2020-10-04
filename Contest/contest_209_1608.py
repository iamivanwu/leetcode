from typing import List
import collections
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter = collections.Counter()
        for i in range(len(nums)):
            for j in range(nums[i]+1):
                counter[j] += 1
        for c in counter:
            if c == counter[c]:
                return c
        return -1