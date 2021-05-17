from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        candiesSum = []
        for candy in candiesCount:
            if not candiesSum:
                candiesSum.append(candy)
            else:
                candiesSum.append(candiesSum[-1]+candy)
        for query in queries:
            eatmax = (query[1]+1)*query[2]
            eatmin = query[1]+1
            low = candiesSum[query[0]] - candiesCount[query[0]] + 1
            high = candiesSum[query[0]]
            if high >= eatmin and low <= eatmax:
                res.append(True)
            else:
                res.append(False)
        return res
candiesCount = [7,4,5,3,8]
queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
print(Solution().canEat(candiesCount,queries))
