class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
        res = 0
        for num in hashmap.values():
            if num > 1:
                res += int(num*(num-1)/2)
        
        return res