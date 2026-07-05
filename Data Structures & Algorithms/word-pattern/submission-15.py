class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w_ch = {}
        ch_w = {}
        words = s.split(' ')

        if len(pattern) != len(words): return False

        for i in range(len(pattern)):
            if (pattern[i] in ch_w and ch_w[pattern[i]] != words[i]) or (words[i] in w_ch and w_ch[words[i]] != pattern[i]):
                return False
            ch_w[pattern[i]] = words[i]
            w_ch[words[i]] = pattern[i]
        
        return True