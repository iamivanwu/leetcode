class Solution:
    def cal(self, a, b):
        if b == 0:
            return 1
        temp = self.cal(a,b//2)
        if b % 2 == 0:
            return temp * temp
        else:
            return temp * temp * a

    def myPow(self, x: float, n: int) -> float:
        if n >= 0 :
            ans = self.cal(x, n)
        else :
            ans = self.cal(1/x, -n)
        return ans

# 2^10 = 2^5 * 2^5
a = 0.00001
b = 2147483647
sol = Solution()
print(sol.myPow(a,b))