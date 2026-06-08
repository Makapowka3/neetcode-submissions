class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        for n in hashmap:
            if hashmap[n] % 2 != 0:
                return False
        return True