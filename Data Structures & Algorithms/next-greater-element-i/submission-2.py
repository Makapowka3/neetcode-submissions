class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        output = []
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        for n1 in nums1:
            greater = False
            for n2 in nums2[hashmap[n1]:]:
                if n2 > n1:
                    output.append(n2)
                    greater = True
                    break
            if not greater:
                output.append(-1)
        return output
