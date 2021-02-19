class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp,cnt = '',0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
                temp += s[i]
            elif s[i] == ')':
                if cnt > 0:
                    cnt -= 1
                    temp += s[i]
            else:
                temp += s[i]
        res,cnt = '',0
        for i in range(len(temp)-1,-1,-1):
            if temp[i] == ')':
                cnt += 1
                res = temp[i] + res
            elif temp[i] == '(':
                if cnt > 0:
                    cnt -= 1
                    res = temp[i] + res
            else:
                res = temp[i] + res
        return res