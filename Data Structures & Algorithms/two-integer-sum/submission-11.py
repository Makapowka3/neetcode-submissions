class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        counter = 0
        for num in nums:
            if num in hash_map:
                hash_map[num] += [counter]
                return hash_map[num]
            else:
                hash_map[target - num] = [counter]
            counter += 1
        return []