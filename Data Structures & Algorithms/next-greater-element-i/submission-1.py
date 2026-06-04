class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                v = stack.pop()
                next_greater[v] = n
            stack.append(n)
        
        while stack:
            v = stack.pop()
            next_greater[v] = -1

        res = []
        for n in nums1:
            res.append(next_greater[n])
        
        return res