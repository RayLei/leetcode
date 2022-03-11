class StockPrice:

    def __init__(self):
        self.timestamps = []
        self.prices = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamps:
            idx = self.timestamps.index(timestamp)
            self.prices[idx] = price
        else:
            self.timestamps.append(timestamp)
            self.prices.append(price)

    def current(self) -> int:
        return self.prices[-1]

    def maximum(self) -> int:
        return max(self.prices)

    def minimum(self) -> int:
        return min(self.prices)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

["StockPrice","update","maximum","current","minimum","maximum","maximum","maximum","minimum","minimum","maximum","update","maximum","minimum","update","maximum","minimum","current","maximum","update","minimum","maximum","update","maximum","maximum","current","update","current","minimum","update","update","minimum","minimum","update","current","update","maximum","update","minimum"]
[[],[38,2308],[],[],[],[],[],[],[],[],[],[47,7876],[],[],[58,1866],[],[],[],[],[43,121],[],[],[40,5339],[],[],[],[32,5339],[],[],[43,6414],[49,9369],[],[],[36,3192],[],[48,1006],[],[53,8013],[]]
