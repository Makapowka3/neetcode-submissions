class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        n = len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for v, fre in freq.items():
            buckets[fre].append(v)
        
        ret = []
        for f in range(n, 0, -1):
            for num in buckets[f]:
                ret.append(num)
                if len(ret) >= k:
                    return ret