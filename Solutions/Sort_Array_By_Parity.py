from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        odd = []
        for n in A:
            if n % 2:
                odd.append(n)
            else:
                ans.append(n)
        return ans + odd