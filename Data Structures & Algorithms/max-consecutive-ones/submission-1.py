class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones, running = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running += 1
            else:
                running, max_ones = 0, max(max_ones, running)
        return max(max_ones, running)