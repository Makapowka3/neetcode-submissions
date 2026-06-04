class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        min_diff = max(nums)
        nums.sort()
        p1, p2 = 0, k - 1
        while p2 < len(nums):
            m = nums[p2]
            n = nums[p1]
            min_diff = min(min_diff, m - n)
            p2 += 1
            p1 += 1
        return min_diff
