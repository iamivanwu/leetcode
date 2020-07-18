from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxP,minP = prices[0],prices[0]
        pro = []
        for p in prices:
            if minP > p:
                maxP = p
                minP = p
            if maxP < p:
                maxP = p
            pro.append(maxP-minP)
        return max(pro)
            
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))