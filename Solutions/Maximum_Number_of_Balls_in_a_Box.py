from collections import Counter
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counter = Counter()
        for i in range(lowLimit,highLimit+1):
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
            counter[s] += 1
        return counter.most_common()[0][1]