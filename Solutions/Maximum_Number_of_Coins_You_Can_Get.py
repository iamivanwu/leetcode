from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        pile_num = len(piles)//3
        ans = 0
        index = len(piles)-1
        sorted_piles = sorted(piles)
        while pile_num:
            ans += sorted_piles[index-1]
            index -= 2
            pile_num -= 1
        return ans
