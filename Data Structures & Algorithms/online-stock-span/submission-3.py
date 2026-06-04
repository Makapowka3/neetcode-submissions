class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
        self.index = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(self.index)
            self.prices.append(price)
            self.index += 1
            return 1
        self.prices.append(price)
        while self.stack and price >= self.prices[self.stack[-1]]:
            self.stack.pop()
        self.stack.append(self.index)
        if len(self.stack) > 1:
            res = self.stack[-1] - self.stack[-2]
        else:
            res = self.stack[-1] + 1
        self.index += 1
        return res


        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)