class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = defaultdict(int)

        for num in arr:
            hashmap[num] += 1
        
        res = -1
        for k, v in hashmap.items():
            if k == v:
                res = max(res, k)
        return res