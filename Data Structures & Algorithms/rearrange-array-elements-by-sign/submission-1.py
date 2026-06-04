class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        res = [0] * len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                res[even] = nums[k]
                even += 2
            else:
                res[odd] = nums[k]
                odd += 2
        return res