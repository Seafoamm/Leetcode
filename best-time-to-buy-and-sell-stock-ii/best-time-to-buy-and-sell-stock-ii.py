class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        if len(prices) == 0:
            return 0
        prev = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prev:
                totalProfit += prices[i] - prev
            prev = prices[i]
            
        
        return totalProfit