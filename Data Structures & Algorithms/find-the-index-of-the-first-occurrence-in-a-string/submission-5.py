class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0,0

        while p1 < len(haystack):
            if haystack[p1] == needle[p2]:
                p2 += 1
                p1 += 1
                if p2 == len(needle):
                    return p1 - p2

            elif p2 == 0:
                p1 += 1
            
            else:
                p1 -= p2 - 1
                p2 = 0
        
        return -1