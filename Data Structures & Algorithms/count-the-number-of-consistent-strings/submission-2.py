class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashset = set(allowed)

        res = len(words)
        for w in words:
            for ch in w:
                if ch not in hashset:
                    res -= 1
                    break
        
        return res