class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #target is to maximize volume 
        #bruteforce->multiply each pair  -> and track the max
        #use 2 pointer and see whether area changes when we shift lower or higher bar
        maxvol=0
        i,j=0,len(heights)-1
        while i<j:
            vol=min(heights[i],heights[j])*(j-i)
            maxvol=max(vol,maxvol)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxvol
        