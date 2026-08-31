class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #start from begining i poiner is buy and one is sell , if buy < sell then it is a profit , if not then move the buy to sell (because if the profit is not positive that means selling price is lowest)
        l=0 #buy
        r=1 #sell
        maxp=0
        while r<len(prices):
            if prices[l]< prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(profit,maxp)
            else:
                l=r
            r+=1
                
        return maxp
            
        