from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
        count = 0
        last = 0
        for t in target:
            if t > target:
                count += t - last
            last = t
        return count