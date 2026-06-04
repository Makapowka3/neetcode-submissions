class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        def findMin(nums: List[int]) -> int:
            lower, upper = 0, len(nums) - 1
            while lower < upper:
                middle = (lower + upper) // 2
                if nums[middle] > nums[upper]:
                    lower = middle + 1
                else:
                    upper = middle 
            return lower
        if nums[-1] == target:
            return len(nums) - 1
        if nums[-1] > target:
            lower, upper = findMin(nums), len(nums) - 1
        else:
            lower, upper = 0, findMin(nums) - 1
        while lower <= upper:
            middle = (lower + upper) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                upper = middle - 1
            else:
                lower = middle + 1
        return -1
        

        