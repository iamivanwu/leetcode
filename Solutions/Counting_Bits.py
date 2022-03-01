from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            ans.append(ans[int(i/2)] + (i & 1))
        return ans
print(Solution().countBits(1000))