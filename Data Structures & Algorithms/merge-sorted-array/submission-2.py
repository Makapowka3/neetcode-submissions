class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m+n-1
        p1, p2 = len(nums1)-n-1, len(nums2) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1
            k -= 1
        
        while p2 >= 0:
            nums1[k] = nums2[p2]
            k -= 1
            p2 -= 1
        
        