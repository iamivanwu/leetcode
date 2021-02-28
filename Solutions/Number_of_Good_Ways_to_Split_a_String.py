import collections
class Solution:
    def numSplits(self, s: str) -> int:
        counter = collections.Counter()
        for c in s:
            counter[c] += 1
        left = collections.Counter()
        count = 0
        counter = dict(counter)
        for i in range(len(s)-1):
            left[s[i]] += 1
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                counter.pop(s[i])
            if len(list(left.keys())) == len(list(counter.keys())):
                count += 1
        return count

s = "aacaba"
print(Solution().numSplits(s))