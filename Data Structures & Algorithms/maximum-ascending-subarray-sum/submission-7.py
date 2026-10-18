class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        running_sum, max_sum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                running_sum += nums[i]
            else:
                max_sum = max(max_sum, running_sum)
                running_sum = nums[i]

        return max(max_sum, running_sum)