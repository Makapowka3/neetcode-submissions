class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words_sorted = sorted(words, key=len)
        #Go left to right checking whether the word is a prefix of some other word
        #store them in some list
        storage = set()
        for i in range(len(words_sorted)):
            for j in range(i+1, len(words_sorted)):
                if words_sorted[i] in words_sorted[j]:
                    storage.add(words_sorted[i])
        return list(storage)