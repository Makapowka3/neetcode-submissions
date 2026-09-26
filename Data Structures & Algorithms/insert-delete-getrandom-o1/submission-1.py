class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.l)
            self.l.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            self.l[-1], self.l[idx] = self.l[idx], self.l[-1]
            self.hashmap[self.l[idx]] = idx 
            self.l.pop()
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        n = random.choice(self.l)
        return n


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()