from typing import List
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weak = []
        for i in range(len(mat)):
            heapq.heappush(weak,(sum(mat[i]),i))
        return [x for _,x in heapq.nsmallest(k,weak)]