class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        res = 0
        for w in words:
            if w[:length] == pref:
                res += 1
        
        return res