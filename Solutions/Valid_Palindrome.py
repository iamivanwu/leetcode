class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l <= r:
            if not s[l].isalpha() and not s[l].isnumeric():
                l += 1
            elif not s[r].isalpha() and not s[r].isnumeric():
                r -= 1
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        return True
s = "1A man, a plan, a canal: Panama1"
print(Solution().isPalindrome(s))