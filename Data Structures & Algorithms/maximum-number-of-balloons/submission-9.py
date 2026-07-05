class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = set(['b', 'a', 'l', 'o', 'n'])
        hash1 = Counter(text)
        
        res = float('inf')
        for el in balloon:
            if el == 'l' or el == 'o':
                res = min(res, hash1[el]//2)
            else:
                res = min(res, hash1[el])
        
        return res if res < len(text) else 0