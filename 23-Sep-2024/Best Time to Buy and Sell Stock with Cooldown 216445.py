# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dp(idx,buy):
            ans=0
            if idx >= len(prices):
                return 0
            if (idx,buy) in memo:
                return memo[(idx,buy)]
            if buy:
                buy_item= dp(idx+1,0)-prices[idx]
                not_buy=dp(idx+1,1)
                ans=max(buy_item,not_buy)
            else:
                sell_item=dp(idx+2,1) + prices[idx]
                not_sell=dp(idx+1,0)
                ans=max(sell_item,not_sell)
            memo[(idx,buy)]=ans

            return ans
        return dp(0,1)
        
        