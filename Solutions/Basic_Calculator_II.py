class Solution:
    def calculate(self, s: str) -> int:
        def md():
            self.need = False
            second = num.pop()
            first = num.pop()
            ope = op.pop()
            if ope == '*':
                return num.append(first*second)
            else:
                return num.append(first//second)
        num = []
        op = []
        last = ""
        self.need = False
        for c in s:
            if c == " ":
                last = ""
                continue
            if c == '+' or c == '-':
                if self.need:
                    md()
                op.append(c)
                last = ""
                continue
            if c == '*' or c == '/':
                if self.need:
                    md()
                self.need = True
                op.append(c)
                last = ""
                continue
            if last != "":
                last = num.pop()
                n = str(last) + c
            else:
                n = c
            num.append(int(n))
            last = n
        if self.need:
            md()
        for oper in op:
            first = num.pop(0)
            second = num.pop(0)
            if oper == '+':
                num.insert(0, first + second)
            else:
                num.insert(0, first - second)
        return(num[0])

s = " 32+2*2+2"
s = " 3/2 "
s = "2/2-1"
s = "1+1-1"
# s = "0-2147483647"
sol = Solution()
print(sol.calculate(s))