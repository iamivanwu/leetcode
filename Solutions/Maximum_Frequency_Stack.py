import collections
class FreqStack:

    def __init__(self):
        self.stack = collections.defaultdict(list)
        self.counter = collections.Counter()
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.counter[x] += 1
        freq = self.counter[x]
        self.maxfreq = max(self.maxfreq, freq)
        self.stack[freq].append(x)

    def pop(self) -> int:
        x = self.stack[self.maxfreq].pop()
        self.counter[x] -= 1
        if not self.stack[self.maxfreq]:
            self.maxfreq -= 1
        return x