class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        for i in range(0, n):
            if i < 2:
                prime[i] = False
                continue
            if prime[i] == False:
                continue
            for j in range(i * i, n, i):
                prime[j] = False
        return sum(prime)

n = 10
n = 2
sol = Solution()
print(sol.countPrimes(n))