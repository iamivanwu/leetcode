from typing import List
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pair_table = {}
        for i,j in pairs:
           pair_table[i] = j
           pair_table[j] = i
        ans = 0
        for i in range(n):
            for j in preferences[i]:
                if j == pair_table[i]:
                    break
                if preferences[j].index(i) < preferences[j].index(pair_table[j]):
                    ans += 1
                    break
        return ans
n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
print(Solution().unhappyFriends(n,preferences,pairs))