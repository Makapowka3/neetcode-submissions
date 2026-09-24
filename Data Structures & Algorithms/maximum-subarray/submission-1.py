class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        trailing = 0

        for n in nums:
            if trailing < 0:
                trailing = 0
            trailing += n
            res = max(res, trailing)
        
        return res