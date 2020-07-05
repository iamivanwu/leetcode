from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # arr = []
        # ants = 0
        # for i in range(0, n+1):
        #     arr.append(0)
        # for r in range(0, len(right)):
        #     arr[right[r]] = 1
        #     ants = ants + 1
        # for l in range(0, len(left)):
        #     arr[left[l]] = -1
        #     ants = ants + 1
        # print(arr)
        # step = 0
        # while ants > 0:
        #     for i
        max = -1
        for i in range(0, len(left)):
            if left[i] > max:
                max = left[i]
        for i in range(0, len(right)):
            if n - right[i] > max:
                max = n - right[i]
        return max

       
n = 20
left = [4,7,15]
right = [9,3,13,10]
sol = Solution()
#  17
print(sol.getLastMoment(n, left, right))