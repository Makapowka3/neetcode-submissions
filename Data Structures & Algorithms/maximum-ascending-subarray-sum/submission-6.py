class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        running = 0

        for i in range(len(nums)-1):

            if nums[i] < nums[i+1]:
                ascend = True
                running += nums[i]
            else:
                res = max(res, running + nums[i])
                running = 0
        
        res = max(res, running + nums[-1])
        
        return res