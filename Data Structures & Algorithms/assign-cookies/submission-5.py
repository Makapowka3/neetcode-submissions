class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        p_g, p_s = 0, 0
        count = 0

        while p_s < len(s) and p_g < len(g):
            if g[p_g] <= s[p_s]:
                p_g += 1
                count += 1
            p_s += 1
            
        return count