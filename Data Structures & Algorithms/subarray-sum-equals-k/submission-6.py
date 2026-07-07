class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for val in prefix:
            hashmap[val] += 1

        res = 0

        for i in range(len(prefix) - 1, -1, -1):
            hashmap[prefix[i]] -= 1

            target = prefix[i] - k
            res += hashmap[target]
        
        return res