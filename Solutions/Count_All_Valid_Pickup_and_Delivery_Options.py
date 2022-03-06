class Solution:
    def countOrders(self, n: int) -> int:
        def factory(x):
            res = 1
            for i in range(0, x):
                res *= i + 1
            return res

        res = factory(2 * n)
        for _ in range(n):
            res = res >> 1
        return res % (10**9 + 7)


print(Solution().countOrders(3))
