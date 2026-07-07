class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_c = s.count('1')
        res = []

        for i in range(one_c-1):
            res.append(str(1))
        
        for i in range(len(s)-one_c):
            res.append(str(0))
        
        res.append(str(1))
        return ''.join(res)