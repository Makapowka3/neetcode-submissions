class Solution:
    def maxScore(self, s: str) -> int:
        left = [0,]
        right = [0,]

        for i in range(len(s)):
            left.append(left[-1] + (s[i] == "0"))
            right.append(right[-1] + (s[len(s) - i - 1] == "1"))
        
        res = 0
        for i in range(len(s)-1):
            res = max(res, left[i+1] + right[len(s)-i-1])
        
        return res

                