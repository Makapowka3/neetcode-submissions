class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write = 0
        read = 1
        while read < len(nums):
            if nums[read] != nums[write]:
                nums[write + 1] = nums[read]
                write += 1
            read += 1
        return write + 1