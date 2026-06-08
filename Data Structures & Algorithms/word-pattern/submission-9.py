class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_s = {}
        s_to_p = {}

        s = s.split(' ')
        if len(s) != len(pattern): return False
        for word, ch in zip(s, pattern):
            if word in s_to_p and s_to_p[word] != ch:
                return False
            s_to_p[word] = ch
            if ch in p_to_s and p_to_s[ch] != word:
                return False
            p_to_s[ch] = word
        return True