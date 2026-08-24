class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """ build a hashmap as a default dict that will have counts of each character mapped to the words 
        then to calculate the count for each letter and have a mapping you use ordinal mapping ,
        when you got that count array set up now populate that count array
        now append that count array as a key and the word as a value in the hashmap
        then return the last list"""
        hashm=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            hashm[tuple(count)].append(s)
        return list(hashm.values())