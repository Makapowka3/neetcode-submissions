class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
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
        
        for item in dict_s:
            if item not in dict_t:
                return False
            if dict_t[item] != dict_s[item]:
                return False
        return True