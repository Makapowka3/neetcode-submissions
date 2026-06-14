class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        res = 0
        for word in words:
            consistent = True
            for ch in word:
                if ch not in allowed_set:
                    consistent = False
                    break
            if consistent:
                res += 1

        return res                