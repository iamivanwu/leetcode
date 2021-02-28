from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for customer in accounts:
            money = 0
            for bank in customer:
                money += bank
            res = max(res, money)
        return res