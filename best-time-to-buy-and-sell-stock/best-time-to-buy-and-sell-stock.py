class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = float('inf')
        
        profit = 0
        
        for price in prices:
            if price < start:
                start = price
            profit = max(profit, price - start)
            
        
        
        
        return profit