class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set(i for i in range(1, len(nums) + 1))
        for num in nums:
            if num in hashset:
                hashset.remove(num)
        return list(hashset)