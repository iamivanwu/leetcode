from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        interval = 0
        for i in range(1, len(arr)):
            if i == 1:
                interval = arr[i] - arr[i-1]
                continue
            if interval != arr[i] - arr[i-1]:
                return False
            interval = arr[i] - arr[i-1]
        return True

            


# arr = [3,5,1]
arr = [1,2,4]
sol = Solution()
print(sol.canMakeArithmeticProgression(arr))