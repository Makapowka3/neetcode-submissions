class Solution:
    def maxDifference(self, s: str) -> int:
        freq_count = defaultdict(int)
        for ch in s:
            freq_count[ch] += 1
        max_odd, min_even = 0, len(s)
        for v in freq_count.values():
            if v%2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        return max_odd - min_even