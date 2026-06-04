class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_mag = {}
        hash_rans = {}
        
        for ch in magazine:
            if ch in hash_mag:
                hash_mag[ch] += 1
            else:
                hash_mag[ch] = 1
        
        for ch in ransomNote:
            if ch in hash_rans:
                hash_rans[ch] += 1
            else:
                hash_rans[ch] = 1
        
        for k, v in hash_rans.items():
            if k in hash_mag:
                if hash_mag[k] < v:
                    return False
            else:
                return False
        
        return True