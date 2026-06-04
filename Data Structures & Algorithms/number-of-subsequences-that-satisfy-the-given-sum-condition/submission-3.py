class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        p1, p2 = 0, len(nums) - 1
        counter = 0
        while p1 <= p2:
            min1, max1 = nums[p1], nums[p2]
            if min1 + max1 <= target:
                counter += 2**(p2-p1)
                p1 += 1
            else:
                p2 -= 1
        return counter % ((10**9) + 7)
                