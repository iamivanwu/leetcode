import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        collect = collections.Counter(s)
        ans = 0
        arr = [0 for _ in range(100000)]
        for col in collect:
            arr[collect[col]] += 1
        for i in reversed(range(100000)):
            if arr[i] > 1 and i != 0:
                ans += arr[i]-1
                arr[i-1] += arr[i]-1
        return ans

print(Solution().minDeletions("abcabc"))