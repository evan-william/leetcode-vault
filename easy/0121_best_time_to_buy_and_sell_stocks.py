class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # update founded lowest value 
            if price < min_price:
                min_price = price
            
            # instantly count profit with today
            profit = price - min_price
            
            # ipdate max profit
            if profit > max_profit:
                max_profit = profit
                
        return max_profit