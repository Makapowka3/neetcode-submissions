class Solution:
    def maxScore(self, s: str) -> int:
        right_ones = 0
        left_zeros = 1 if s[0] == '0' else 0

        for i in range(1,len(s)):
            if s[i] == '1':
                right_ones += 1
        
        res = 0
        for i in range(1, len(s)):
            res = max(res, left_zeros + right_ones)
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
        
        return res