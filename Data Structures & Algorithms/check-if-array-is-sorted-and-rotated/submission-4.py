class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                drops += 1

        return drops == 0 or (drops == 1 and nums[-1] <= nums[0])