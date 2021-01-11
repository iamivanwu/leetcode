from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        now = 0
        dp = [0]
        while now < amount:
            now += 1
            count = 0
            for coin in coins:
                if coin == now:
                    count = 1
                elif coin < now and dp[now-coin] > 0:
                    if count != 0:
                        count = min(count,dp[now-coin]+1)
                    else:
                        count = dp[now-coin] + 1
            dp.append(count)
        return dp[-1] if dp[-1] > 0 else -1
coins = [1,2,5]
amount = 100
print(Solution().coinChange(coins,amount))