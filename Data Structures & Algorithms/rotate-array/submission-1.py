class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        temp = nums[:]
        for i in range(n):
            nums[(i + k) % n] = temp[i]