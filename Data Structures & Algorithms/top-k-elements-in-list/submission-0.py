class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """build a frequency hashmap 
           convert the hashmap to a list
           sort the list in scending order
           run a while loop with len of the list > k
           and then get the last element's 2nd element and store it in result"
           """
        hashm={}
        for i in nums:
            if i in hashm:
                hashm[i]+=1
            else:
                hashm[i]=1
        listss=[]
        for num,cnt in hashm.items():
            listss.append([cnt,num])
        listss.sort()

        res=[]
        while len(res)<k:
            values=listss.pop()[1]
            res.append(values)
        return res

