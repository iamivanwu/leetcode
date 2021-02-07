class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        abc = sorted([a,b,c])
        if abc[2] - abc[1] >= abc[0]:
            abc[1] += abc[0]
        else:
            abc[0] -= abc[2] - abc[1]
            abc[1] += abc[2] - abc[1]
            abc[1] += (abc[0]+1)//2
            abc[2] += abc[0] // 2
        return min(abc[1],abc[2])