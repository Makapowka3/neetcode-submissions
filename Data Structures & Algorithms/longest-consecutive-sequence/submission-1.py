class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hash_num = set(nums)
        longest = 1
        for v in nums:
            if v in hash_num:
                l = 1
                while v - 1 in hash_num:
                    v -= 1
                while v + 1 in hash_num:
                    l += 1
                    hash_num.remove(v)
                    v += 1
                longest = max(longest, l)
        return longest