class Solution:
    def minFlips(self, target: str) -> int:
        last = '0'
        count = 0
        for i in range(len(target)):
            if target[i] != last:
                count += 1
            last = target[i]
        return count
print(Solution().minFlips("00000"))