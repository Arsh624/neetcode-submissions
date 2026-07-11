class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            hashs={}
            hashm={}
            for ch in s:
                if ch in hashs:
                    hashs[ch]+=1
                else:
                    hashs[ch]=1
            for c in t:
                if c in hashm:
                    hashm[c]+=1
                else:
                    hashm[c]=1
            if hashs==hashm:
                return True
            else:
                return False