class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, 0 
        start = 0
        while p1 < len(haystack) and p2 < len(needle):
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            else:
                start += 1
                p1 = start
                p2 = 0

        if p2 == len(needle):
            return start
            
        return -1
