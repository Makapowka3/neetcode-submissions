class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]].append(i)
            else:
                hashmap[s[i]] = [i,]
        
        res = -1
        for l in hashmap.values():
            if len(l) > 1:
                res = max(res, max(l) - min(l) - 1)
        
        return res