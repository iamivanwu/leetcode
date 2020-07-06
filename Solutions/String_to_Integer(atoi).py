import re
class Solution:
    def myAtoi(self, str: str) -> int:
        numRe = re.match(r'[\+\-0]*[0-9]+', str.strip())
        try:
            if int(numRe.group()) < -2147483648:
                return -2147483648
            elif int(numRe.group()) > 2147483648-1:
                return 2147483648-1
            return int(numRe.group())
        except:
            return 0


sol = Solution()
str = "04193 with words"
print(sol.myAtoi(str))