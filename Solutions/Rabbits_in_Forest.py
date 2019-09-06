from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = {}
        num = 0
        for ans in answers:
            if s.get(ans):
                s[ans] += 1
                if s.get(ans) > ans + 1:
                    num += ans + 1
                    s[ans] = 1
            else:
                s[ans] = 1
        for a in s:
            num += a + 1
        return num



answers = [1, 1, 2]
answers = [1,0,1,0,0]
# answers = []
answers = [0,0,1,1,1]
sol = Solution()
print(sol.numRabbits(answers))