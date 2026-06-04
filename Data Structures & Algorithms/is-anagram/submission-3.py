class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in dict1:
                dict1[ch] += 1
            else:
                dict1[ch] = 1
        for ch in t:
            if ch in dict1:
                dict1[ch] -=1
            else:
                return False
        for v in dict1:
            if dict1[v] == 0:
                continue
            else:
                return False
        return True
