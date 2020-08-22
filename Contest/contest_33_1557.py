from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = [0]*n
        for _,j in edges:
            visited[j] = 1
        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)
        return ans