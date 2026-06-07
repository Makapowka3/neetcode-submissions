class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        max_res = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_res = max(max_res, inc, dec)
        
        return max_res
