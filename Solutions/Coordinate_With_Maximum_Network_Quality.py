from typing import List
import math
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_q = 0
        res_x,res_y = 0,0
        for x,y,_ in towers:
            sum_q = 0
            for x2,y2,q2 in towers:
                d = math.sqrt(abs((x2-x)*(x2-x)+(y2-y)*(y2-y)))
                if d <= radius:
                    sum_q += int(q2//(1+d))
            if sum_q > max_q:
                res_x,res_y = x,y
                max_q = sum_q
            elif sum_q == max_q:
                if x < res_x or (x == res_x and y < res_y):
                    res_x,res_y = x,y
        return [res_x,res_y]
towers = [[28,6,30],[23,16,0],[21,42,22],[50,33,34],[14,7,50],[40,31,4],[39,45,17],[46,21,12],[45,36,45],[35,43,43],[29,41,48],[22,27,5],[42,44,45],[10,49,50],[47,43,26],[40,36,25],[10,25,6],[27,30,30],[50,35,20],[11,0,44],[34,29,28]]
radius = 12
print(Solution().bestCoordinate(towers,radius))