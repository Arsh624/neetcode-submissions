class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        see the point is - we dont nee dto replace it literaly in this question -> we just wanna know the longest valid window that can have those replacemnts  so if this condition :
        replacement numbers=len(curr substring) - freq of highest is less than eqal to the K , it is valid, so we jsut need to track the max of these windows 



        """
        counter={}
        l=0
        res=0
        for r in range(len(s)):
            # make a freq counter first
            counter[s[r]]= 1+ counter.get(s[r],0) 

            #check condition if the window is NOT valid
            while (r-l+1) - max(counter.values()) >k:
                counter[s[l]]-=1
                l+=1
            res=max(res,r-l+1) 
        return res




