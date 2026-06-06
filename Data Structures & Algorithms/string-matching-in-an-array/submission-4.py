class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_sorted = sorted(words, key=len)
        storage = []
        for i in range(len(words_sorted)):
            for j in range(i+1, len(words_sorted)):
                if words_sorted[i] in words_sorted[j]:
                    storage.append(words_sorted[i])
                    break
        return storage