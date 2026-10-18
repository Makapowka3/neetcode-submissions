class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)

        for ch in ransomNote:
            if ch in hashmap:
                hashmap[ch] -= 1
                if hashmap[ch] < 0:
                    return False
            else:
                return False
        
        return True