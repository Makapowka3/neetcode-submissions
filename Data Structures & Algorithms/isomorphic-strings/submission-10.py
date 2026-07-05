class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in range(len(s)):
            if s[i] in hash1:
                if hash1[s[i]] != t[i]:
                    return False
            else:
                hash1[s[i]] = t[i]
            
            if t[i] in hash2:
                if hash2[t[i]] != s[i]:
                    return False
            else:
                hash2[t[i]] = s[i]
        
        return True