class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operator = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num *10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                operator = s[i]
        return sum(stack)

s = " 32+2*2+2"
s = " 3/2 "
# s = "2/2-1"
# s = "1+1-1"
# s = "0/1"
# s = "0-2147483647"
s = "14-3/2"
sol = Solution()
print(sol.calculate(s))