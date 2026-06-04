class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest, running = 0, 1
        current = 1
        p1 = 1
        while p1 < len(nums):
            if nums[p1] == nums[p1 - 1]:
                p1 += 1
                longest = max(longest, running)
                running = 1
                continue
            if nums[p1] > nums[p1 - 1] and current == 1:
                running += 1
            elif nums[p1] > nums[p1 - 1] and current == -1:
                longest = max(longest, running)
                running = 2
                current = 1
            elif nums[p1] < nums[p1 - 1] and current == -1:
                running += 1
            else:
                longest = max(longest, running)
                running = 2
                current = -1
            p1 += 1
        longest = max(longest, running)
        return longest