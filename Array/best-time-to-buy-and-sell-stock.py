class Solution:
    def maxProfit(self, prices):
        buy, profit, bought = 0, 0, False
        for price in prices:
            if price < buy or not bought:
                buy = price
                bought = True
            elif profit < price - buy and bought:
                profit = price - buy
        return profit
