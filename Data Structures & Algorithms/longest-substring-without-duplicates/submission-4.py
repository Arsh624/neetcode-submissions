class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        input-> s 
        return -> length of longest substring wothiut duplicates
        substring is contigous  
        z x y z x y z
        i 
          j
        """
        charset=set()
        res=0 
        l,r = 0,0
        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res=max(res,r-l+1)
            r+=1
        return res 
        











    
        # charset=set()
        # mp={}
        # l=0
        # res=0
        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l=max()
        #     mp[s[r]]
        #     res=max(res,len(charset))

        # return res
































        # #we are using set  to make sure we aave a data structure that has only unique values - also keep in mind that sets are unordered -> so right pointer goes in traversing while left stays at the start  , lrigth check WHILE the duplicate is there inside the set , we traverse and remove that value(since its contigious so we remove everything before the duplicate as well)
        
        # charset= set()
        # res=0
        # l=0
        # for r in range(len(s)):
        #     while s[r] in charset:
        #         charset.remove(s[l])
        #         l+=1
        #     charset.add(s[r])
        #     res=max(len(charset),res)
        # return res




        