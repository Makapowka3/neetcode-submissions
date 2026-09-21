class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        
        dp = [0,1,1]

        for i in range(n-2):
            dp.append(dp[-3] + dp[-2] + dp[-1])
        
        return dp[-1]