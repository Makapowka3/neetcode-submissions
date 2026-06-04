class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1 = set()
        hash2 = set()
        
        for num in nums1:
            hash1.add(num)
        for num in nums2:
            hash2.add(num)
        
        return [list(hash1-hash2),list(hash2-hash1)]