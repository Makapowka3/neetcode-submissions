class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]

        for i in range(len(cost)-1):
            dp.append(min(dp[-2] + cost[i], dp[-1] + cost[i+1]))
        
        return dp[-1]