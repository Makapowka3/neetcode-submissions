class MyHashSet:

    def __init__(self):
        self.m = 2000
        self.buckets = [[] for _ in range(self.m)]
    def idx_(self, key):
        return key % self.m

    def add(self, key: int) -> None:
        b = self.buckets[self.idx_(key)]
        if key not in b:
            b.append(key)
        return

    def remove(self, key: int) -> None:
        b = self.buckets[self.idx_(key)]
        for i, x in enumerate(b):
            if x == key:
                b.pop(i)
                return

    def contains(self, key: int) -> bool:
        if key in self.buckets[self.idx_(key)]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)