class Solution:
    def scoreOfString(self, s: str) -> int:
        p1, p2 = 0, 1
        
        res = 0
        while p2 < len(s):
            res += abs(ord(s[p2]) - ord(s[p1]))
            p1 += 1
            p2 += 1
        
        return res