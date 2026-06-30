class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n = abs(n)
            if nums[n] < 0:
                return n
            else:
                nums[n] = -nums[n]
        