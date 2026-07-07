class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for n in nums:
            curr = 1
            temp = n
            while n + 1 in hashset:
                curr += 1
                hashset.remove(n+1)
                n += 1
            while temp - 1 in hashset:
                curr += 1
                hashset.remove(temp-1)
                temp -= 1
            res = max(res, curr)
        
        return res