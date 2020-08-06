from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter()
        for n in nums:
            counter[n] += 1
            if counter[n] > len(nums)//2:
                return n
