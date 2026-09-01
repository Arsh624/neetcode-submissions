class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        permu=[]
        for c in s1:
            permu.append(ord(c)-ord("a"))
        r=len(s1)-1
        for l in range(len(s2)):
            if r>=len(s2):
                break
            permu2=[]
            for c in range(l,r+1):
                permu2.append(ord(s2[c])-ord("a"))
            if sorted(permu) == sorted(permu2):
                return True
            
            r+=1
        return False

            

            