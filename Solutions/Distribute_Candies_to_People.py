from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [0]*num_people
        num = 0
        while candies > 0:
            num += 1 
            candies -= num
            arr[(num-1)%num_people] += num
            if candies < 0:
                arr[(num-1)%num_people] += candies
        return arr