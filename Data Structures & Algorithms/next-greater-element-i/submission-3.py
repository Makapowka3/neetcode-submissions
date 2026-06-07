class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Build a monotonic stack for nums2
        #Assign the next greater element for each element in nums2
        #Then go through nums1 and just lookup the dict
        hashmap = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)
        
        while stack:
            hashmap[stack.pop()] = -1
        
        res = []
        for num in nums1:
            res.append(hashmap[num])
        
        return res
        
        