class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 2: return nums
        p1, p2 = 0, 1

        while p2 < len(nums):
            while p2 < len(nums) and nums[p1] == 0:
                if nums[p2] == 0:
                    p2 += 1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1 
        
        