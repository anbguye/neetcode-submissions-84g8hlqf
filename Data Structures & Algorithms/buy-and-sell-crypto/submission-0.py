class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = -1
        l = 0

        for r in range(len(prices)):

            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r
        
        return max_profit
