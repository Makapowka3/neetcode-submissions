class Solution:
    def scoreOfString(self, s: str) -> int:
        running = 0
        for i in range(1, len(s)):
            running += abs(ord(s[i-1]) - ord(s[i]))
        return running