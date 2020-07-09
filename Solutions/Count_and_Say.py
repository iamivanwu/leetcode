class Solution:
    def countAndSay(self, n: int) -> str:
        a = ['1']
        for i in range(1,n):
            count = 0
            s = ''
            last = a[i-1][0]
            for c in a[i-1]:
                if c != last:
                    s = s + str(count) + last
                    last = c
                    count = 1
                else: 
                    count += 1
            s = s + str(count) + last
            a.append(s)
        return a[-1]

n = 8
print(Solution().countAndSay(n))