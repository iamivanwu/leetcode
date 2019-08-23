from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def find(node,path):
            path.append(node)
            if node == len(graph) - 1:
                return a.append(path.copy())
            for n in graph[node]:
                temp = path.copy()
                path.append(find(n,path))
                path = temp

        a = []
        for i in range(len(graph[0])):
            path = []
            path.append(0)
            find(graph[0][i],path)
        return a
    
        

nums = [[1,2], [2,3], [3], []]
sol = Solution()
print(sol.allPathsSourceTarget(nums))