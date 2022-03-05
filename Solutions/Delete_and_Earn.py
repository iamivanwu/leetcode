from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(sorted(nums))
        take, noTake = 0, 0
        for key in counter.keys():
            take, noTake = (
                max(
                    key * counter[key] + noTake,
                    key * counter[key] + take - (key - 1) * counter[key - 1],
                ),
                take,
            )
        return max(take, noTake)


print(Solution().deleteAndEarn([3, 3, 3, 4, 2]))
