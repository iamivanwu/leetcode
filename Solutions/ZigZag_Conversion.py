class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        for r in range(0,numRows):
            if int(len(s)/numRows) == 0 or numRows == 1:
                return s
            for i in range(0,int(len(s)/numRows)+1):
                if r+(2*numRows-2)*i >= len(s):
                    continue
                ans = ans + s[r+(2*numRows-2)*i]
                if (r != 0) and 2*numRows-2-r != r:
                    if 2*numRows-2-r + (2*numRows-2)*i >= len(s):
                        continue
                    ans = ans +s[2*numRows-2-r + (2*numRows-2)*i]
        return ans
s = "PAYPALISHIRING"
# s = "ABC"
numRows = 3
sol = Solution()
print(sol.convert(s,numRows))