class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        for n in nums:
            hash_map[n] += 1
        for k, v in hash_map.items():
            if v > len(nums)/2:
                return k