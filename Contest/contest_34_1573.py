class Solution:
    def numWays(self, s: str) -> int:
        total = s.count('1')
        if total % 3 != 0:
            return 0
        if total == 0:
            return (len(s)-1)*(len(s)-2)/2 % 1000000007
        now = 0
        zero = 0
        zeros = []
        a = 0
        for c in s:
            if c == '1' and a == 2:
                break
            if c == '1':
                if now == total // 3:
                    a += 1
                    now = 0
                    zeros.append(zero)
                    zero = 0
                now += 1
            if c == '0' and now == total // 3:
                zero += 1
        return (zeros[0]+1)*(zeros[1]+1) % 1000000007
s = "100100010100110"
# s = "00000"
s = "00000000"
print(Solution().numWays(s))