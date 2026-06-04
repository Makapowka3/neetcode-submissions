class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        res = []
        for k, v in freq.items():
            if v > len(nums)/3:
                res.append(k)
        
        return res