from typing import List
from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m = len(candyType) // 2
        candies = Counter(candyType)
        return min(len(candies),m)