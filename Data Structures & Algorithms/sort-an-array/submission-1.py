class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            combined = []
            i = 0
            j = 0
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    combined.append(l1[i])
                    i += 1
                else:
                    combined.append(l2[j])
                    j += 1
            while i < len(l1):
                combined.append(l1[i])
                i += 1
            while j < len(l2):
                combined.append(l2[j])
                j += 1
            return combined
        
        if len(nums) <= 1:
            return nums
        mid_index = len(nums) // 2
        left = self.sortArray(nums[:mid_index])
        right = self.sortArray(nums[mid_index:])
        return merge(left,right)