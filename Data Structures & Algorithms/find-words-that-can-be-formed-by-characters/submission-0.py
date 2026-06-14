class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        hashmap = defaultdict(int)
        for c in chars:
            hashmap[c] += 1
        
        for w in words:
            word_dict = defaultdict(int)
            good = True
            for ch in w:
                word_dict[ch] += 1
                if word_dict[ch] > hashmap[ch]:
                    good = False
            if good:
                res += len(w)
        
        return res
