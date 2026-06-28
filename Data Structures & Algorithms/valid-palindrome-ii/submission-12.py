class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if s[p1] != s[p2]:
                return is_palindrome(p1 + 1, p2) or is_palindrome(p1, p2 - 1)

            p1 += 1
            p2 -= 1

        return True
