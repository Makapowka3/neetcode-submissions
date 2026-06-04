class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p1, p2 = len(s), len(s) - 1 
        space = False
        while p2 > -1:
            if s[p2] != ' ':
                space = True
                p2 -= 1
            else:
                if space:
                    p2 += 1
                    break
                p1 = p2
                p2 -= 1
        if p2 == -1:
            p2 = 0
        return p1-p2