class Solution:
    def mySqrt(self, x: int) -> int:
        if x * x == x : return x
        l = 0
        r = x
        mid = (l + r) // 2
        while mid != l:
            if mid * mid > x:
                r = (l + r) // 2
            else:
                l = (l + r) // 2
            mid = (l + r) // 2
        return mid

# 8 -> 4 -> 2 -> 3
a = 9
sol = Solution()
print (sol.mySqrt(a))