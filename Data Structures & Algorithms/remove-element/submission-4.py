class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        read, write = 0, len(nums)-1
        while read < write:
            if nums[read] == val:
                nums[read], nums[write] = nums[write], nums[read]
                write -= 1
            else:
                read += 1
        if nums[read] == val: return read
        return read+1