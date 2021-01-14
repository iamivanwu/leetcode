import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.set.get(val):
            return False
        else:
            self.set[val] = 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.set.get(val):
            self.set.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        values = list(self.set.keys())
        return values[random.randint(0,len(values)-1)]
        
