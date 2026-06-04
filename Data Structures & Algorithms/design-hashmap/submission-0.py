class MyHashMap:

    def __init__(self):
        self.m = 5000
        self.buckets = [[] for _ in range(self.m)]
    
    def idx(self, num):
        return num % self.m
        

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self.idx(key)]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
         

    def get(self, key: int) -> int:
        bucket = self.buckets[self.idx(key)]
        for t in bucket:
            if t[0] == key:
                return t[1]
        return -1
        

    def remove(self, key: int) -> None:
        bucket = self.buckets[self.idx(key)]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)