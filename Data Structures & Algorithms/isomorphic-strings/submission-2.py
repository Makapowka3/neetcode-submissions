class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map1 = {}
        char_map2 = {}
        p1, p2 = 0, 0
        
        while p1 < len(s):
            if s[p1] in char_map1:
                if char_map1[s[p1]] == t[p2]:
                    pass
                else:
                    return False
            else:
                char_map1[s[p1]] = t[p2]

            if t[p2] in char_map2:
                if char_map2[t[p2]] == s[p1]:
                    pass
                else:
                    return False
            else:
                char_map2[t[p2]] = s[p1]
              
            p1 += 1
            p2 += 1

        return True