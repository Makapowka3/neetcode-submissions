class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(i for i in range(1, len(nums)+1))
        for n in nums:
            if n in num_set:
                num_set.remove(n)
        return list(num_set)