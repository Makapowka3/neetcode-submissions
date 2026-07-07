class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            if total%k in hashmap:
                if i - hashmap[total%k] > 1:
                    return True
            else:
                hashmap[total%k] = i

        return False