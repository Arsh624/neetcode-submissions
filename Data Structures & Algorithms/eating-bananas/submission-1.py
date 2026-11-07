class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        input-> [ 1, 2 ,3, 4,5] max allowed hours h=9
        k is speed = 4
        
        time = ceil(banana / speed)  

        """
        l ,r = 1, max(piles)
        res= r
        while l<=r:
            speed = l+(r-l)//2
            totaltime=0
            for banana in piles:
                totaltime += math.ceil(float(banana)/speed)
            if totaltime <= h:
                res=speed
                r = speed - 1 
            else:
                l = speed + 1
        return res
        



        
        