class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ s = "racecar", t = "carrace" """
        if len(s)==len(t):
            counter1={}
            counter2={}
            for x in s:
                if x in counter1:
                    counter1[x]+=1
                else:
                    counter1[x]=1
            for y in t:
                if y in counter2:
                    counter2[y]+=1
                else:
                    counter2[y]=1
            if counter1==counter2:
                return True
            else:
                return False
        else:
            return False

