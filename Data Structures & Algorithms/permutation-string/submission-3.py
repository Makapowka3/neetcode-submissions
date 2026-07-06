class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        l1 = [0] * 26
        l2 = [0] * 26

        for i in range(len(s1)):
            l1[ord(s1[i]) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if l1 == l2:
                return True
            l2[ord(s2[r]) - ord('a')] += 1
            l2[ord(s2[l]) - ord('a')] -= 1
            l += 1
        
        return l1 == l2