class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash1 = Counter(chars)

        res = 0
        for word in words:
            curr_w = Counter(word)
            good = True
            
            for el in curr_w:
                if curr_w[el] > hash1[el]:
                    good = False
            
            if good:
                res += len(word)
        
        return res