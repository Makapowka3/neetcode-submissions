class Solution:
    def customSortString(self, order: str, s: str) -> str:  
        others = ''
        relative = {}
        counter = 0
        for ch in order:
            relative[ch] = counter
            counter += 1

        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            elif ch in order:
                freq[ch] = 1
            else:
                others += ch
        
        res = ''
        for ch in relative:
            if ch in freq:
                count = freq[ch]
                res += count * ch
        res += others
        
        return res
