class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        p1, p2 = 0, 1
        while p2 < len(s):
            summ += abs(ord(s[p1])-ord(s[p2]))
            p1 += 1
            p2 += 1
        return summ