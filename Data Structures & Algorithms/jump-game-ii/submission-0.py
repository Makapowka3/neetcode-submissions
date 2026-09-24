class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(i+1, nums[i] + i + 1):
                if j < len(nums):
                    if dp[j] != 0:
                        dp[j] = min(dp[i] + 1, dp[j])
                    else:
                        dp[j] = dp[i] + 1
        
        return dp[-1]