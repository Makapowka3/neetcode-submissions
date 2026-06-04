class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        n = len(nums)
        k %= n
        l, r = 0, k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r = k, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
