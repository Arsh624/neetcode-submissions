class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        


        buy=0
        sell=1
        maxp=0
        while sell<len(prices):
            if prices[buy] > prices[sell]:
                buy=sell
            else:
                prof=prices[sell]-prices[buy]
                maxp=max(maxp,prof)
            sell+=1
                

        return maxp
































        # l=0 #buy
        # r=1 #sell
        # maxp=0
        # while r<len(prices):
        #     if prices[l]< prices[r]:
        #         profit=prices[r]-prices[l]
        #         maxp=max(profit,maxp)
        #     else:
        #         l=r
        #     r+=1
                
        # return maxp
            
        