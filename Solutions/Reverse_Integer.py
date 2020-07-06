class Solution:
    def reverse(self, x: int) -> int:
        signed = True
        s = str(x)
        if s[0] == '-':
            signed = False
        ans = ''
        for i in range(0,len(s)):
            if i == 0:
                if not signed:
                    ans = ans + '-'
                else:
                    ans = ans + '+'
            elif i == len(s) -1 and not signed:
                break
            ans = ans + s[len(s)-1-i]
        if int(ans) < -2147483648 or int(ans) > 2147483648-1:
            return 0
        return(int(ans))


sol = Solution()
print(sol.reverse(1534236469))