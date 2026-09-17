class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        """
        bruteforce - 
        - sort eac h of the string  [ act, opst , opst ....]
        - store in hashm = {act : [act,cat],opst:[pots,tops,stop],aht:[hat] }
        return hashm.values()
        """
        # hashm=defaultdict(list) #space- o(n*m) 
        # for s in strs:
        #     sortedS="".join(sorted(s)) m*nlogn
        #     hashm[sortedS].append(s)
        # return list(hashm.values())

        """ build a hashmap as a default dict that will have counts ofeach        character mapped to the words then to calculate the count for each letter and have a mapping you use ordinal mapping , when you got that count array set up now populate that count array now append that count array as a key( we convert that list count to a tuple because in python list cannot be keys) and the word as a value in the hashmap then return the last list"""

        hashm=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            hashm[tuple(count)].append(s)
        return list(hashm.values())

        