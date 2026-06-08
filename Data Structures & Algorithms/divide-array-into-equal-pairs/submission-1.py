class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_set = set()
        
        for n in nums:
            if n in freq_set:
                freq_set.remove(n)
            else:
                freq_set.add(n)
        
        return not freq_set