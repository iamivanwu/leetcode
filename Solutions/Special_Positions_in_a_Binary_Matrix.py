from typing import List
import collections
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sum_row = []
        for i in range(len(mat)):
            sum_row.append(sum(mat[i]))
        sum_col = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                sum_col[j] += mat[i][j]
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if sum_row[i] == 1 and sum_col[j] == 1:
                        ans += 1
        
        return ans
mat = [[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]
print(Solution().numSpecial(mat))