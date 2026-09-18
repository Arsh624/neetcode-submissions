class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        bruteforce- 
        charset=set()
        condition = be unique
        l , r = 0 , 1
        check in the window whether condition is there
        - if not - move l+1 and r+1
        - if yes - r+1 
        """
        charSet=set()
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(len(charSet),res)
        return res
            

































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




        