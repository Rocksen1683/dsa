class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #variable length sliding window as we don't know length of window 

        #global max profit 
        maxProfit = 0 
        curProfit = 0 

        l = 0 #left pointer 

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                curProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, curProfit)
            else:
                #reset day to buy
                l = r

        return maxProfit