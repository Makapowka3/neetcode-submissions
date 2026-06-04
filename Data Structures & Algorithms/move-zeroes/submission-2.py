class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        n = len(nums)
        for n in nums:
            if n != 0:
                nums[write] = n
                write += 1
        while write < len(nums):
            nums[write] = 0
            write += 1
        