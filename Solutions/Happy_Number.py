class Solution:
    def isHappy(self, n: int) -> bool:
        table = {}
        while n != 1:
            if table.get(n):
                return False
            else:
                table[n] = 1
            cal = 0
            while n != 0:
                cal += (n%10)*(n%10)
                n = n // 10
            n = cal
        return True
print(Solution().isHappy(4))