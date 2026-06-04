class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        for ch in t:
            if ch in dict2:
                dict2[ch] += 1
            else:
                dict2[ch] = 1
        for v in dict1:
            if v in dict2:
                if dict1[v] == dict2[v]:
                    continue
                else: return False
            else: return False
        return True
                