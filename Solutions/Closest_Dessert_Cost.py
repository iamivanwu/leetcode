from typing import List
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = float('-inf')
        mabs = float('inf')
        for base in baseCosts:
            cost = [base]
            for top in toppingCosts:
                temp = cost
                cost = []
                for c in temp:
                    if not c in cost and c - target <= mabs:
                        mabs = min(mabs,abs(c - target))
                        cost.append(c)
                    if not c + top in cost and c + top - target <= mabs: 
                        mabs = min(mabs,abs(c + top - target))
                        cost.append(c + top)
                    if not c + 2*top in cost and c + 2 * top - target <= mabs:
                        mabs = min(mabs,abs(c + 2*top - target))
                        cost.append(c + 2*top)
            for c in cost:
                if target == c:
                    return c
                if abs(target - c) < (abs(target-res)):
                    res = c
                elif abs(target - c) == (abs(target-res)):
                    res = min(res, c)
        return res
baseCosts = [1,7]
toppingCosts = [3,4]
target = 10
print(Solution().closestCost(baseCosts,toppingCosts,target))
                        