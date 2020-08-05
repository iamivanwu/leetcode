class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''
        if numerator % denominator == 0:
            return str(numerator//denominator)
        if numerator*denominator < 0:
            ans += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        q = numerator//denominator
        numerator -= q*denominator
        ans += str(q) + '.'
        qtable = {}
        i = len(ans)
        while numerator != 0:
            if not qtable.get(numerator):
                qtable[numerator] = i
            else:
                i = qtable.get(numerator)
                ans = ans[:i] + '(' + ans[i:] + ')'
                break            
            if numerator < denominator:
                numerator *= 10
            q = numerator//denominator            
            numerator = (numerator - q*denominator)
            ans += str(q)
            i += 1
            print(qtable)
        return ans
a = 1
b = 6
print(Solution().fractionToDecimal(a,b))