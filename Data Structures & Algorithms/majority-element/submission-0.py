class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_c = {}
        for num in nums:
            if num in dict_c:
                dict_c[num] += 1
            else:
                dict_c[num] = 1
        for k, v in dict_c.items():
            if v > len(nums) / 2:
                return k
        return None