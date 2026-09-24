class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if not dp[i]:
                continue

            for jump in range(1, nums[i] + 1):
                if i + jump >= len(nums) - 1:
                    return True

                dp[i + jump] = True

        return dp[-1]