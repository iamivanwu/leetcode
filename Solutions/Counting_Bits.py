from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(sum(int(c) for c in bin(i)[2:] if c == '1'))
        return ans
print(Solution().countBits(1000))