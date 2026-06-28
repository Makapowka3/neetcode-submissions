class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = Counter(text)
        bal_set = set(['b', 'a', 'l', 'o', 'n'])

        res = float('inf')
        for ch in bal_set:
            if ch == 'l' or ch == 'o':
                res = min(res, hashmap[ch]//2)
            else:
                res = min(res, hashmap[ch])
        
        if res > len(text):
            return 0
        
        return res