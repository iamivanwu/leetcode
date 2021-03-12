class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        code = set()
        for i in range(k,len(s)+1):
            code.add(s[i-k:i])
            if len(code) == pow(2,k):
                return True
        return False

s = "0000000001011100"
k = 4
print(Solution().hasAllCodes(s,k))