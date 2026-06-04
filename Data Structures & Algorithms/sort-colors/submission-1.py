class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = 0
        p2 = len(nums) - 1
        read = 0

        while read <= p2:
            print(p0, read, p2)
            if nums[read] == 0:
                nums[p0], nums[read] = nums[read], nums[p0]
                p0 += 1
                read += 1
            elif nums[read] == 2:
                nums[p2], nums[read] = nums[read], nums[p2]
                p2 -= 1
            else:
                read += 1
        