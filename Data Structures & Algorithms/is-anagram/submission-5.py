class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for ch in s:
            if ch in dict_s:
                dict_s[ch] += 1
            else:
                dict_s[ch] = 1

        for ch in t:
            if ch in dict_t:
                dict_t[ch] += 1
            else:
                dict_t[ch] = 1
        
        for key, value in dict_s.items():
            if key not in dict_t:
                return False
            if value != dict_t[key]:
                return False
                
        return len(s) == len(t)