from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float('inf')
        ans = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > fee:
                ans += prices[i] - buy - fee
                buy = prices[i] - fee
        return ans