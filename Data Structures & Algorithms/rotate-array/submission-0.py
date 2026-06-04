class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr = {}
        for i, num in enumerate(nums):
            arr[num] = (i + k) % len(nums)
        p1 = 0
        for k, v in arr.items():
            nums[v] = k
        