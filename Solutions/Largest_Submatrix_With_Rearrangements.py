from typing import List
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
            now = sorted(matrix[i],reverse=True)
            for j in range(len(now)):
                m = max(m,(j+1)*now[j])
        return m

matrix = [[0,0,1],[1,1,1],[1,0,1]]
print(Solution().largestSubmatrix(matrix))