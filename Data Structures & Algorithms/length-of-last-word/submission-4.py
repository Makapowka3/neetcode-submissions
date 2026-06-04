class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while s[i] == ' ':
            i -= 1
        
        word_len = 0

        while i >= 0 and s[i] != ' ':
            word_len += 1
            i -= 1
        
        return word_len
