class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        is_inc = None
        if nums[-1] < nums[0]:
            is_inc = False
        else:
            is_inc = True

        if is_inc:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    return False
        
        return True