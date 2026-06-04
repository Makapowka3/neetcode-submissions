class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_sorted = sorted(words, key=len)
        res = []
        for i in range(len(words_sorted)):
            w = words_sorted[i]
            for j in range(i + 1, len(words_sorted)):
                if w in words_sorted[j]:
                    res.append(w)
                    break
        return res