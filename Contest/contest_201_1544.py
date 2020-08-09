class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ''
        ans = [s[0]]
        for i in range(1,len(s)):
            if len(ans)>0 and ans[-1].lower() == s[i].lower() and ans[-1] != s[i]:
                ans.pop()
            else:
                ans.append(s[i])
        return ''.join(ans)