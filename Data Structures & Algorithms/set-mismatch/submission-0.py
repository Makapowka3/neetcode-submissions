class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        finder = set(i+1 for i in range(len(nums)))

        for n in nums:
            if n not in finder:
                twice = n
            else:
                finder.remove(n)
        
        for el in finder:
            missing = el

        return [twice, missing]