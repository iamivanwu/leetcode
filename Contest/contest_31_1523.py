class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1:
            return low % 2 + (high - low)//2
        else:
            return high % 2 + (high - low)//2