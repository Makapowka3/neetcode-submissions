class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, blue = 0, len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
                i += 1
            elif nums[i] == 2:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
            else:
                i += 1

        