class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = defaultdict(int)

        for ch in s:
            char_count[ch] += 1
        
        res = []
        for ch in order:
            for _ in range(char_count[ch]):
                res.append(ch)
        
        for ch in s:
            if ch not in order:
                res.append(ch)
        
        return ''.join(res)

        