class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #target is to maximize volume 
        #bruteforce->multiply each pair  -> and track the max
        #use 2 pointer and see whether area changes when we shift lower or higher bar


        """
        - aim is to maximize area 
        - 2  pointers  - left and right 
        """
        l,r =0 , len(heights)-1
        maxar=0
        while l < r:
            if heights[l] > heights[r]:
                area=heights[r]*(r-l)
                maxar=max(maxar,area)
                r-=1
            else:
                area= heights[l] *(r-l)
                maxar= max(maxar,area)
                l+=1
        return maxar
























        left=0
        right=len(heights)-1
        maxarea=0

        while left<right:
            if heights[left]>heights[right]:
                area=(right-left)* heights[right]
                maxarea=max(maxarea,area)
                right-=1
            else:
                area=(right-left)* heights[left]
                maxarea=max(area,maxarea)
                left+=1
        return maxarea
        
        