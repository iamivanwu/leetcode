class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        temp = []
        for c in s:
            if (c in temp):
                if (len(temp) > m):
                    m = len(temp)
                temp = temp[temp.index(c)+1:]
                print(temp)
            temp.append(c)
        print(temp)
        return len(temp) if len(temp) > m else m

sol = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
# s = " "
s = "dvdf"
print(sol.lengthOfLongestSubstring(s))