class LRUCache:
    capacity = 0
    lr = []
    cache = {}
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lr = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.lr:
            self.lr.append(self.lr.pop(self.lr.index(key)))
        return self.cache.get(key,-1)

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if key in self.lr:
            self.lr.append(self.lr.pop(self.lr.index(key)))
        else:
            self.lr.append(key)
        if len(self.cache) > self.capacity:
            self.cache.pop(self.lr[0])
            self.lr.pop(0)
        