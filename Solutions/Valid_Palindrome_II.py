class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isValid(s[:l] + s[l + 1 :]) or isValid(s[:r] + s[r + 1 :])
            l += 1
            r -= 1
        return True


# "ebcbb e cecab bacec bbcbe"
s = "ebcbbececabbacecbbcbe"
s = "cbbcc"
s = "abc"
print(Solution().validPalindrome(s))
