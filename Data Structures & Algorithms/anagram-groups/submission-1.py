class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ build a array that will have counts of each 
        the use that array to buuld a hash map wiht keys as 
        that coutnes and values as the words wiht htose counts"""
        hashm=defaultdict(list)
        for word in strs:
            arr= [0]*26
            for chrs in word:
                arr[ord(chrs) - ord("a")]+=1
            hashm[tuple(arr)].append(word)
        return list(hashm.values())
        
            
