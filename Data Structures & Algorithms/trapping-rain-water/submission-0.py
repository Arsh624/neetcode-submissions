class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1. check the base case
        2. Initiate pointers and values
        3. start the loop
        4. Reasoning: now water ata current point depends on what? -> 
           the minimum of leftmax or right max right? -> so we process
           the side that is minimum because the taller opposite
           boundary is already sufficient to guarantee that the
           smaller maximum determines the water level.   
        """
        if not height:
            return 0
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        res=0
        while l < r:
            if lmax < rmax:
                #we move before processing to avoid the inital start 
                res += lmax - height[l]
                l+=1
                lmax = max(lmax,height[l])
            else:
                res+= rmax - height[r]
                r-=1
                rmax= max(rmax , height[r])

        return res



