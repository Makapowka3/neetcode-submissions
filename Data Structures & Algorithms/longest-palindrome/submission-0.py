class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = defaultdict(int)
        
        for ch in s:
            hashmap[ch] += 1
        
        res = 0
        for ch in hashmap:
            res += hashmap[ch] - hashmap[ch] % 2
        if res < len(s):
            res += 1

        return res