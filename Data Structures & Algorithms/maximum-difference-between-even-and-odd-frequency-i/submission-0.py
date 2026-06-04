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
        max_odd, min_even = 0, len(s)
        for k, v in freq_map.items():
            if v % 2 != 0:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        
        return max_odd - min_even