class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = Counter(s)
        hash2 = Counter(t)

        for el in hash1:
            if hash1[el] != hash2[el]:
                return False
        
        for el in hash2:
            if hash2[el] != hash1[el]:
                return False
        
        return True