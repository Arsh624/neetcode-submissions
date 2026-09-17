class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        Bruteforce
        - we check len(s)=!len(t):return False
        - sorteds=sorted(s) and sorted(t) o(nlogn+mlogm) space- O(n+m) o(1)
        - if sorted(s)==sorted(t) - return true 
        - else false
        """
        if len(s)!=len(t):
            return False
        mapping=26*[0] #abc - > 11100000

        for i in range(len(s)):
            mapping[ord(s[i])-ord('a')]+=1
            mapping[ord(t[i])-ord('a')]-=1

        for val in mapping: 
            if val!=0:
                return False
        return True

        

        





        