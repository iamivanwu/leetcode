from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        draw = {}
        def dfs(p):
            for p2 in graph[p]:
                if p2 in draw:
                    if draw[p2] == draw[p]:
                        return False
                else:
                    draw[p2] = 1 - draw[p]
                    if not dfs(p2):
                        return False
            return True
        for i in range(len(graph)):
            if i not in draw:
                draw[i] = 0
            if not dfs(i):
                return False
        return True
