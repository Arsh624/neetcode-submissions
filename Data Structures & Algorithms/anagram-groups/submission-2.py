class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ build a hashmap that will have counts of each 
        the use that array to buuld a hash map wiht keys as 
        that coutnes and values as the words wiht htose counts"""
        hashm=defaultdict(list)
        for word in strs:
            count=[0]*26 #(1a...1c...1t..0z)
            for ch in word:
                count[ord(ch)-ord("a")]+=1
            hashm[tuple(count)].append(word)
        return list(hashm.values())
        
            
