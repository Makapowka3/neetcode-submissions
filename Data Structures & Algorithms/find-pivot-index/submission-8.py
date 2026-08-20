class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0] * (len(nums)+1)
        right_sum = [0] * (len(nums)+1)

        for i in range(len(nums)):
            left_sum[i+1] = left_sum[i] + nums[i]
            right_sum[i+1] = right_sum[i] + nums[len(nums)-i-1]
        
        for i in range(len(nums)):
            if left_sum[i] == right_sum[len(nums)-i-1]:
                return i
        
        return -1