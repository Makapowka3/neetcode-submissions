class MyHashSet:

    def __init__(self):
        self.hashset = [None]

    def add(self, key: int) -> None:
        if len(self.hashset) < key:
            self.hashset.extend((key-len(self.hashset))*[None])
        self.hashset[key-1] = key
        return

    def remove(self, key: int) -> None:
        if len(self.hashset) >= key:
            self.hashset[key-1] = None
        return

    def contains(self, key: int) -> bool:
        if len(self.hashset) >= key:
            if self.hashset[key-1] is not None:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)