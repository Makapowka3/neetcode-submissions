class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        max_lucky = -1
        for k, v in hashmap.items():
            if k == v:
                max_lucky = max(max_lucky, k)
        
        return max_lucky