from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        count2 = Counter()
        stack = []
        for c in s:
            count2[c] += 1
            if c in stack:
                continue
            while stack and stack[-1] > c and count2[stack[-1]] < count[stack[-1]]:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

s = "cbacdcbc"
s = "abacb"
print(Solution().removeDuplicateLetters(s))