class Solution:
    def modifyString(self, s: str) -> str:
        ans = ''
        last = 'a'
        for i in range(len(s)):
            print(ord(last))
            if s[i] == '?':
                n = ord(last)+1
                if i+1 < len(s) and n == ord(s[i+1]):
                    n += 1
                if n > 122:
                    n = n - 122 + 96
                ans += chr(n)
                last = chr(n)
            else:
                ans += s[i]
                last = s[i]
        return ans
s = "?zs"
print(Solution().modifyString(s))