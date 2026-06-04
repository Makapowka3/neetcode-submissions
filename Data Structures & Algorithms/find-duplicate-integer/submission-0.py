class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = len(nums) * [False]
        p1 = 0
        while True:
            p1 = nums[p1]
            if seen[p1] == True:
                return p1
            seen[p1] = True