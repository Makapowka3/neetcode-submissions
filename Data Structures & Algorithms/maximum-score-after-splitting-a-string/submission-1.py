class Solution:
    def maxScore(self, s: str) -> int:
        left = [0,]
        right = [0,]

        for i in range(len(s)):
            if s[i] == '0':
                left.append(left[-1]+1)
            else:
                left.append(left[-1])
            
            if s[len(s)-i-1] == '1':
                right.append(right[-1]+1)
            else:
                right.append(right[-1])
        print(left,right)
        
        res = 0
        for i in range(len(s)-1):
            res = max(res, left[i+1] + right[len(s)-i-1])
        
        return res

                