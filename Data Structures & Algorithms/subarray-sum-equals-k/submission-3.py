class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        hashmap = {0: 1}
        occur = 0

        for num in nums:
            running_sum += num

            if running_sum - k in hashmap:
                occur += hashmap[running_sum-k]

            if running_sum in hashmap:
                hashmap[running_sum] += 1
            else:
                hashmap[running_sum] = 1
        
        return occur
