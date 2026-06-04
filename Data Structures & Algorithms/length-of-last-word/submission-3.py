class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word_len = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                return word_len
            word_len += 1
        return word_len