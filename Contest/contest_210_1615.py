from typing import List
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        link = [[]for _ in range(n)]
        ranks = [0]*n
        for x,y in roads:
            link[x].append(y)
            link[y].append(x)
            ranks[x] += 1
            ranks[y] += 1
        max_rank = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    rank = ranks[i] + ranks[j]
                    if j in link[i]:
                        rank -= 1
                    max_rank = max(max_rank,rank)
        return max_rank
n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
print(Solution().maximalNetworkRank(n,roads))