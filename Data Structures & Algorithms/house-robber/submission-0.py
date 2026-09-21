class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0]

        for i in range(len(nums)):
            dp.append(max(dp[-2] + nums[i], dp[-1]))
        
        return dp[-1]
