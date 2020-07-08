class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sign = (dividend < 0) is (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor) 
        if divisor == 1:
            if not sign:
                dividend = -dividend
            return min(max(-2147483648, dividend),2147483647)
        while dividend - divisor >= 0:
            ds,a = divisor,1
            while ds < dividend:
                if dividend - (ds << 1) < 0:
                    break
                else:
                    ds <<= 1
                    a <<= 1
            dividend -= ds
            ans += a
        if not sign:
            ans = -ans
        return min(max(-2147483648, ans),2147483647)
dividend = 10
divisor =  3
print(Solution().divide(dividend,divisor))