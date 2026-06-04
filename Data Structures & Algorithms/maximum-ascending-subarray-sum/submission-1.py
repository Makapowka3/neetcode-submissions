class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        inc = 1
        running = nums[0]
        ans = running

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                running += nums[i] 
            else:
                running = nums[i]
            ans = max(ans, running)
        
        return ans