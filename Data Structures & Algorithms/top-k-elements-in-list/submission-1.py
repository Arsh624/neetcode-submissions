class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        """build a frequency hashmap 
           convert the hashmap to a list
           sort the list in scending order
           run a while loop with len of the list > k
           and then get the last element's 2nd element and store it in result"
        """
        freq=Counter(nums)
        pairs=[]
        for nm, cnt in freq.items():
            pairs.append([cnt,nm])
        pairs.sort()
        res=[]
        while len(res)<k:
            res.append(pairs.pop()[1])
        return res


