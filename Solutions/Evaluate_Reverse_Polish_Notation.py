from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t.lstrip('-').isnumeric():
                nums.append(int(t))
            else:
                second = nums.pop()
                first = nums.pop()
                if t == '+':
                    ans = first + second
                elif t == '-':
                    ans = first - second
                elif t == '*':
                    ans = first * second
                else:
                    neg = first*second < 0
                    ans = abs(first) // abs(second)
                    if neg:
                        ans = -ans
                nums.append(ans)
        return nums[-1]