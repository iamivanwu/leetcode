from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = 0
        s,index = 1,0
        while n < k:
            if index < len(arr) and arr[index] == s:
                index += 1
            else:
                n += 1
            s += 1
        return s-1