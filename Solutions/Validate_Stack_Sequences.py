from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        temp = []
        for i in range(len(pushed)):
            if pushed[i] == popped[j]:
                j += 1
            else:
                while temp and j < len(popped)  and temp[-1] == popped[j]:
                    temp.pop()
                    j += 1
                temp.append(pushed[i])
        while temp and j < len(popped)  and temp[-1] == popped[j]:
            temp.pop()
            j += 1
        return j == len(popped)
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(Solution().validateStackSequences(pushed,popped))