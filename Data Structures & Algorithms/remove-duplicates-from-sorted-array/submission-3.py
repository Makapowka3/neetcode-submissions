class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 1, 0
        while read < len(nums):
            if nums[read] != nums[write]:
                nums[write+1] = nums[read]
                write += 1
            read += 1
        return write+1