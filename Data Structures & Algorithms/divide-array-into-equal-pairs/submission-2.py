class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)

        for el in hashmap:
            if hashmap[el] % 2 == 1:
                return False

        if len(nums) % 2 == 0:
            return True
        else:
            return False