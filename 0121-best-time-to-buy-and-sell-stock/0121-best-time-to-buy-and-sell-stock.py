class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        minn = prices[0]
        for i in range(1,n):
            profit = prices[i]-minn
            max_profit = max(profit,max_profit)
            minn = min(minn,prices[i])
        return max_profit    
        