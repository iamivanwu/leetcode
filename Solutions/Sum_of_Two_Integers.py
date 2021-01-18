class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            c = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = c
        return a if a <= MAX else ~(a ^ mask)

a = -2
b = 1
print(Solution().getSum(a,b))