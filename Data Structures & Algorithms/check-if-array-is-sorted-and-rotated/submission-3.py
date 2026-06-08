class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        pivot_count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot_count += 1
        
        if pivot_count == 0:
            return True
        elif pivot_count == 1 and nums[-1] <= nums[0]:
            return True
        return False