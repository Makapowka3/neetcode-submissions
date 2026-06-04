class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_mag = {}
        
        for ch in magazine:
            if ch in hash_mag:
                hash_mag[ch] += 1
            else:
                hash_mag[ch] = 1
        
        for ch in ransomNote:
            if ch in hash_mag:
                if hash_mag[ch] > 0:
                    hash_mag[ch] -= 1
                else:
                    return False
            else:
                return False    
        
        return True