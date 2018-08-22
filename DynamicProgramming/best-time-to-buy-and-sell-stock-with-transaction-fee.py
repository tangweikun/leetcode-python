# HELP:
class Solution:
    def maxProfit(self, prices, fee):
        cash, hold = 0, prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, prices[i] - hold - fee)
            hold = min(hold, prices[i] - cash)
        return cash
