from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        while i < len(matrix) and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            if i + 1 < len(matrix):
                if matrix[i + 1][j] <= target:
                    i = i + 1
                else:
                    j = j + 1
            else:
                j = j + 1

        return False
