class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_start = False
        counter = 0
        for i in range(len(s)):
            if s[len(s)-i-1] == ' ':
                if word_start:
                    return counter
            else:
                word_start = True
                counter += 1
        
        return counter