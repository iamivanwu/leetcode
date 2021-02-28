from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        m = arr[0]
        step = 0
        for i in range(1,len(arr)):
            step += 1
            if arr[i] > m:
                step = 1
                m = arr[i]
            if step == k:
                return m
        return m
arr = [2,1,3,5,4,6,7]
k = 2
print(Solution().getWinner(arr,k))