from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if not customers:
            return 0
        people = customers[0]
        customers_index = 0
        # box = [0,0,0,0]
        # box_index = 0
        profit = 0
        max_profit = -1
        max_turn = -1
        turn = 0
        up = 0
        while people > 0 or len(customers)-1 > customers_index:
            if people >= 4:
                people -= 4
                up += 4
            else:
                up += people
                people = 0
            # box[box_index] += up
            turn += 1
            profit = up*boardingCost - turn*runningCost
            if profit > max_profit:
                max_profit = profit
                max_turn = turn
            # max_profit = max(max_profit, profit)
            # box_index = (box_index + 1) % 4
            if len(customers)-1 > customers_index:
                customers_index += 1
                people += customers[customers_index]
        return max_turn

customers = [8,3]
boardingCost = 5
runningCost = 6
customers = [0,43,37,9,23,35,18,7,45,3,8,24,1,6,37,2,38,15,1,14,39,27,4,25,27,33,43,8,44,30,38,40,20,5,17,27,43,11,6,2,30,49,30,25,32,3,18,23,45,43,30,14,41,17,42,42,44,38,18,26,32,48,37,5,37,21,2,9,48,48,40,45,25,30,49,41,4,48,40,29,23,17,7,5,44,23,43,9,35,26,44,3,26,16,31,11,9,4,28,49,43,39,9,39,37,7,6,7,16,1,30,2,4,43,23,16,39,5,30,23,39,29,31,26,35,15,5,11,45,44,45,43,4,24,40,7,36,10,10,18,6,20,13,11,20,3,32,49,34,41,13,11,3,13,0,13,44,48,43,23,12,23,2]
boardingCost = 43
runningCost = 54
print(Solution().minOperationsMaxProfit(customers,boardingCost,runningCost))