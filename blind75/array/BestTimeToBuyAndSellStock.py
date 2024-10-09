class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxProfit = 0
        while R < len(prices):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                maxProfit = max(profit, maxProfit)
            else:
                L = R
            R += 1

        return maxProfit