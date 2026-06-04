class Solution:
    def maxDifference(self, s: str) -> int:
        freq_map = {}
        even, odd = [], []
        for st in s:
            if st in freq_map:
                freq_map[st] += 1
            else:
                freq_map[st] = 1
        
        max_diff = 0
        odd, even = [], []
        for k, v in freq_map.items():
            if v % 2 != 0:
                odd.append(v)
            else:
                even.append(v)
        
        return max(odd) - min(even)