class Solution:
    def isValid(self, s: str) -> bool:
        first = []
        dic = {')':-1, '(':1, '[':-2, ']':2, '{':-3, '}':3}
        for i in range(len(s)):
            if (len(first) == 0):
                first.append(dic[s[i]])
            else:
                if (first[-1] + dic[s[i]] == 0):
                    first.pop()
                else:
                    first.append(dic[s[i]])
        if (len(first) == 0):
            return True
        else:
            return False

s = "()[]{}"
# s = "([)]"
s = "{[]}"
sol = Solution()
print (sol.isValid(s))