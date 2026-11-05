class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        """
        input: nums , k 
        output: k most freq elements within the array
        approach: make a heap so in heap the minimum would be on top s make max
        heap and pop till k elements 
        """

        count = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for n , c in count.items():
            buckets[c].append(n)
        
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res



#         count=Counter(nums) """{1:1, 2:2 , 3:3} k=2"""
#         buckets= [[] for i in range(len(nums)+1)] 

#         for n , c in count.items():
#             buckets[c].append(n)  """[  [] , [1] , [2] , [3] , [] , [] , []   ]
# """
#         res=[]
#         for i in range(len(buckets)-1,0,-1):
#             for num in buckets[i]:
#                 res.append(num)
#                 if len(res)==k:
#                     return res
        





  










































        # """build a frequency hashmap 
        #    convert the hashmap to a list
        #    sort the list in scending order
        #    run a while loop with len of the list > k
        #    and then get(pop) the last element's 2nd element and store it in result"
        # """
        # freq=Counter(nums)
        # pairs=[]
        # for nm, cnt in freq.items():
        #     pairs.append([cnt,nm])
        # pairs.sort()
        # res=[]
        # while len(res)<k:
        #     res.append(pairs.pop()[1])
        # return res


