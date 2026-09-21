class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev2 = prev1 = 0

            for num in arr:
                current = max(prev2 + num, prev1)
                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )