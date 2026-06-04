class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        p1 = 0
        p2 = len(s) - 1
        sub = False

        while p1 < p2:
            if s[p1] != s[p2]:
                if is_pal(p1+1, p2) and sub == False:
                    p1 += 1
                    sub = True
                elif is_pal(p1, p2-1) and sub == False:
                    p2 -= 1
                    sub = True
                else:
                    return False
            p1 += 1
            p2 -= 1

        return True