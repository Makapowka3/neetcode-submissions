class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]].append(i)
            else:
                hashmap[s[i]] = [i,]
        
        res = float('inf')
        for l in hashmap.values():
            if len(l) == 1:
                res = min(res, l[0])
        
        if res > len(s):
            res = -1
        
        return res