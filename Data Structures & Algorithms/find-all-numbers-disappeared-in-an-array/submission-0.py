class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        res = []

        for i in range(1, n + 1):
            if i not in hashset:
                res.append(i)
        
        return res