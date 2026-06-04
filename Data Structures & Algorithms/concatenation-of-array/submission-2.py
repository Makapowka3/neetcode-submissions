class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = len(nums) * 2 * [None,]
        for i in range(len(nums)):
            output[i] = nums[i]
            output[i+len(nums)] = nums[i]
        return output