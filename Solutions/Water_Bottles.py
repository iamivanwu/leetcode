class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty = 0
        while numBottles > 0:
            count += numBottles
            empty += numBottles 
            change = empty // numExchange
            numBottles = change
            empty -= change*numExchange 
        return count
print(Solution().numWaterBottles(15,4))