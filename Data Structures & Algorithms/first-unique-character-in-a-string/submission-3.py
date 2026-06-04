class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i, ch in enumerate(s):
            if ch in hashmap and hashmap[ch] != 0:
                hashmap[ch] = 0
            elif ch in hashmap and hashmap[ch] == 0:
                pass
            else:
                hashmap[ch] = i + 1
        
        min_in = float('inf')
        for v in hashmap.values():
            if v != 0:
                min_in = min(min_in, v - 1)
        if min_in < len(s):
            return min_in

        return -1