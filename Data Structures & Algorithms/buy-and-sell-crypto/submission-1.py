class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =0 
        maxProfit = 0 
        for sell in range(len(prices)):
            if prices[buy]<prices[sell]:
               profit = prices[sell]-prices[buy] 
               maxProfit = max(maxProfit,profit)
            
            else:
                buy= sell
            sell+=1
        return maxProfit
                

