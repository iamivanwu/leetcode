from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for row in matrix:
            for num in row:
                heapq.heappush(h,num)
        while k > 0:
            res = heapq.heappop(h)
            k -= 1
        return res
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(Solution().kthSmallest(matrix,k))