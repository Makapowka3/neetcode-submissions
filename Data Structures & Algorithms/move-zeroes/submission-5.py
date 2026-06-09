class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for i in range(len(nums)):
            while nums[i] != 0 and write <= i:
                nums[i], nums[write] = nums[write], nums[i]
                write += 1
        
        