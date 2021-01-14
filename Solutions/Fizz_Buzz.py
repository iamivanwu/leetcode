from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            t = ''
            if not ((i+1) % 3):
                t += 'Fizz'
            if not ((i+1) % 5):
                t += 'Buzz'
            if not t:
                t = str(i+1)
            res.append(t)
        return res
print(Solution().fizzBuzz(15))