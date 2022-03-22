class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        remain = k - n
        num = [1] * n
        index = n - 1
        while remain:
            if remain > 25:
                remain -= 25
                num[index] += 25
            else:
                num[index] += remain
                remain = 0
            index -= 1
        res = ''
        for n in num:
            res += chr(96 + n)
        return res
