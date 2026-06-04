class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1 = 0
        s = set(nums)
        while True:
            p1 = nums[p1]
            if p1 in s:
                s.remove(p1)
            else:
                return p1