class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append('(')
            else:
                temp = 0
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                num = 2*temp if temp else 1
                stack.append(num)
        return sum(stack)