class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            print(lower, upper)
            middle = (lower + upper) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                lower = middle + 1
            else:
                upper = middle - 1
        return lower