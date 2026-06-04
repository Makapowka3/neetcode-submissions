class Solution:
    def search(self, nums: List[int], target: int) -> int:
      lower, upper = 0, len(nums) - 1
      while lower <= upper:
            middle = (lower + upper) // 2
            if target == nums[middle]:
                  return middle
            elif target < nums[middle]:
                  upper = middle - 1
            else:
                  lower = middle + 1
      return -1