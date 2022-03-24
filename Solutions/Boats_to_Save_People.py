from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                j -= 1
                i += 1
            res += 1
        return res if i != j else res + 1


people = [2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10]
limit = 50
# people = [2, 4, 5]
# limit = 5
people = [3, 2, 2, 1]
limit = 3
print(Solution().numRescueBoats(people, limit))
