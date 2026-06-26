class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""   #len(word)+'#'+word 
        for word in strs:
            res+=str(len(word))+"#"+word
        return res  




    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length= int(s[i:j])
            res.append(s[j+1:1+j+length])
            i=1+j+length
        return res
        
""" 
for encoding - before every word just add len(word)+"#" +word and put it in a result string
then for decoding- 
initiate a result array , and i pointer from 0 
then while that i pointer is less than length of encoded string 
put j = i and then check for hashtag with  while encodedstring[j]!="#", 
then calculate the length of the word by using [i:j]
then just append everhything from j+1 to length + j + 1 into the result 
then set the i to the end of the word 
return the solution 
"""
