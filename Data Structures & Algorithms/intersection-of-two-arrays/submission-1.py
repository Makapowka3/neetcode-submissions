class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums1:
            hashmap[num] = 0
        
        for num in nums2:
            if num in hashmap:
                hashmap[num] -= 1   

        res = []
        for k, v in hashmap.items():
            if v < 0:
                res.append(k)
        
        return res