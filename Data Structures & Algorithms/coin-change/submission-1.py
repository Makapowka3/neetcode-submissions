class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)
        c_set = set(coins)

        for i in range(1, amount+1):
            min_n = float('inf')
            for coin in c_set:
                if i - coin >= 0:
                    if dp[i-coin] + 1 < min_n and dp[i-coin] != -1:
                        min_n = dp[i-coin] + 1
                if min_n != float('inf'):
                    dp[i] = min_n
                else:
                    dp[i] = -1
        
        return dp[amount]