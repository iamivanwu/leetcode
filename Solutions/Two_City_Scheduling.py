from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
        res = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(Solution().twoCitySchedCost(costs))
