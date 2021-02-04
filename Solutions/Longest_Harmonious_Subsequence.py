from typing import List
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for c in counter:
            if counter[c+1]:
                res = max(res,(counter[c]+counter[c+1]))
        return res
