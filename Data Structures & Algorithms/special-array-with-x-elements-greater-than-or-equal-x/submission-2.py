class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for x in range(1, n + 1):
            if nums[n - x] >= x:
                if n - x == 0 or nums[n - x - 1] < x:
                    return x

        return -1