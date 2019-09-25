from typing import List
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if len(A) > 1:
            for i in range(len(A) - 1, 0, -1):
                for j in range(len(A[i])):
                    A[i-1][j] = A[i-1][j] + min(A[i][max(0,j-1)],A[i][j],A[i][min(len(A[i])-1,j+1)])
        return min(A[0])



## dynamic programming
## computing from last level
## find min sum
## first time
## [[1,2,3],[11,12,14],[7,8,9]]
B =  [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.minFallingPathSum(B))