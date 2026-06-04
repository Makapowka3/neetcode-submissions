class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]  
        best = 0   
        for p in prices[1:]:
            best = max(best, p - min_price)
            if p < min_price:               
                min_price = p
        return best
