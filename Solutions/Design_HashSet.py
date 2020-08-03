class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000001
        self.hash = [0]*self.size

    def add(self, key: int) -> None:
        self.hash[key % self.size] = 1

    def remove(self, key: int) -> None:
        self.hash[key % self.size] = 0

    def contains(self, key: int) -> bool:
        return bool(self.hash[key % self.size])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)