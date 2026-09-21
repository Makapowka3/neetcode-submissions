class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp1, dp2 = [0,0], [0,0]

        for i in range(len(nums)-1):
            dp1.append(max(dp1[-2] + nums[i], dp1[-1]))
        
        for i in range(1, len(nums)):
            dp2.append(max(dp2[-2] + nums[i], dp2[-1]))

        return max(dp1[-1], dp2[-1])