class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictnums = {}
        for val in nums:
            if val not in dictnums:
                dictnums[val] = 1
            elif val in dictnums:
                return True
        return False
