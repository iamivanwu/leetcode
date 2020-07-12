class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        now = 0
        for i in range(0,len(s)):
            if s[i] == '1':
                now += 1
            else:
                count += (now+1)*now//2
                now = 0
        count += ((now+1)*now)//2
        return count % 1000000007
print(Solution().numSub("101"))