from typing import List
from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        def twoSum(a: List[int], b: List[int]):
            res = Counter()
            for i in range(len(a)):
                for j in range(len(b)):
                    res[a[i]+b[j]] += 1
            return res
        c1,c2,ans = Counter(),Counter(),0
        c1 = twoSum(A,B)
        c2 = twoSum(C,D)
        for c in c1:
            if c2[-c] > 0:
                ans += c1[c] * c2[-c]
        return ans