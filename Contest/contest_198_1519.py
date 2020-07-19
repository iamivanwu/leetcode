from typing import List
import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node,par):
            counter = collections.Counter()
            for child in tree[node]:
                if child == par:
                    continue
                counter += dfs(child,node)
            counter[labels[node]] += 1
            ans[node] = counter[labels[node]]
            return counter

        tree = collections.defaultdict(list)
        for i in range(0,n-1):
            tree[edges[i][1]].append(edges[i][0])
            tree[edges[i][0]].append(edges[i][1])
        print(tree)
        ans = [0]*n
        dfs(0,None)
        return ans
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(Solution().countSubTrees(n,edges,labels))