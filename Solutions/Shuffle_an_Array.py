from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        before = self.arr.copy()
        res = []
        for _ in range(len(self.arr)):
            res.append(before.pop(random.randint(0,len(before)-1)))
        return res