class Solution:
    def nthUglyNumber(self, n: int) -> int:
        k2, k3, k5 = 0,0,0
        k = []
        k.append(1)
        if n <= 1:
            return n
        for i in range(1, n + 1):
            k.append(min(k[k2]*2,k[k3]*3,k[k5]*5))
            if k[i] == k[k2]*2:
                k2 += 1
            if k[i] == k[k3]*3:
                k3 += 1
            if k[i] == k[k5]*5:
                k5 += 1
        return k[n - 1]


n = 10
sol = Solution()
print(sol.nthUglyNumber(n))