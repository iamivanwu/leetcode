from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        prof = 0
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                prof += diff 
        return prof
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))