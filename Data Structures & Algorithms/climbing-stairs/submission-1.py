class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
            
        dp = [1, 2]
        
        for _ in range(n-2):
            dp.append(dp[-2]+dp[-1])
        
        return dp[-1]