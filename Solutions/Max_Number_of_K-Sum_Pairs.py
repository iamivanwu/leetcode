from typing import List
from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        table = Counter()
        res = 0
        for n in nums:
            if table[k-n] > 0:
                table[k-n] -= 1
                res += 1
            else:
                table[n] += 1
        return res