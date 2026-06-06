class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #Defo need to use hashmaps
        #Try to build a dict{letter:[index,]}
        #Do the same for the second word
        #Compare indices as they should be equal

        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]].append(i)
            else:
                hash_s[s[i]] = [i,]

            if t[i] in hash_t:
                hash_t[t[i]].append(i)
            else:
                hash_t[t[i]] = [i,]
        
        if len(hash_s) != len(hash_t):
            return False
        
        for l, l1 in zip(hash_s.values(), hash_t.values()):
            if l != l1:
                return False
        return True
            