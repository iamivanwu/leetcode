from typing import List
from collections import Counter
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        for a in sorted(arr):
            s = 1
            for d in dp:
                if a % d == 0 and dp.get(a/d):
                    s += dp[d] * dp[a/d]
            dp[a] = s
        return sum(dp.values()) % (10**9 + 7)

arr = [2,4,5,10]
arr = [2,4,8]
print(Solution().numFactoredBinaryTrees(arr))