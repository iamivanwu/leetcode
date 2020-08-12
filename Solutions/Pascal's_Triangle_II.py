from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 0:
            return [1]
        last = [1,1]
        for k in range(2,rowIndex+1):
            ans = []
            for i in range(0,k+1):
                if i == 0:
                    ans.append(1)
                elif i == k:
                    ans.append(1)
                else:
                    ans.append(last[i-1] + last[i])
            last = ans.copy()        
        return ans
print(Solution().getRow(0))