class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if target <= nums[middle]:
                upper = middle - 1
            else:
                lower = middle + 1
        n = len(nums)
        pos = lower
        if pos + n//2 < len(nums) and nums[pos + n//2] == target:
            return True
        return False
            