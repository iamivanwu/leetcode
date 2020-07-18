from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        par = []
        for i in range(numRows):
            now = [1]
            if i != 0:
                for j in range(len(par[i-1])-1):
                    now.append(par[i-1][j]+par[i-1][j+1])
                now.append(1)
            par.append(now)
        return par
print(Solution().generate(0))
