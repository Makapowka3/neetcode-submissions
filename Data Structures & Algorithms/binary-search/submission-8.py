class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if nums[middle] == target:
                  return middle
            elif nums[middle] < target:
                  lower = middle + 1
            else:
                  upper = middle - 1
        return -1