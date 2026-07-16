class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        res = 0
        lowestPrice = float('inf')

        for r in range(len(prices)):

            if prices[r] < lowestPrice:
                l = r
                lowestPrice = prices[l]
            
            res = max(res, prices[r] - lowestPrice)
        
        return res