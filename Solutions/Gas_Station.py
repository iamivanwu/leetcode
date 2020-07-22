from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g = 0
        start = 0
        tank = 0
        for i in range(len(gas)):
            g = g + gas[i] - cost[i]
            tank += gas[i]
            if tank - cost[i] >= 0:
                tank -= cost[i]
            else:
                start += 1
                tank = 0
        return -1 if g < 0 or start > len(gas) else start 


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas,cost))