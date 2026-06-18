class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []

        for s in strs:
            key = str(sorted(s))
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s,]
        
        for key in hashmap:
            res.append(hashmap[key])
        
        return res