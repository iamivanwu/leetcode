class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(0,len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            if haystack[i] == needle[0]:
                flag = True
                for j in range(0, len(needle)):
                    if needle[j] != haystack[i+j]:
                        flag = False
                        break
                if flag:
                    return i
        return -1

haystack, needle = "mississippi", "issip"
print(Solution().strStr(haystack, needle))