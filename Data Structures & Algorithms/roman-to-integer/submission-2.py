class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        dict_s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for i in range(len(s)-1):
            if dict_s[s[i]] < dict_s[s[i+1]]:
                res -= dict_s[s[i]]
            else:
                res += dict_s[s[i]]
            
        res += dict_s[s[-1]]

        return res