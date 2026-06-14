class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1, min1 = max(nums), min(nums)

        nums.remove(max1)
        nums.remove(min1)

        max2, min2 = max(nums), min(nums)

        return (max1*max2) - (min1*min2)
