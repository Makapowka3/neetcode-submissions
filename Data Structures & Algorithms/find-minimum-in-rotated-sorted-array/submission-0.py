class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            middle = (lower + upper) // 2
            print(lower, upper, middle)
            if nums[middle] > nums[upper]:
                lower = middle + 1
            else:
                upper = middle 
            print('end', lower)
        return nums[lower]
                