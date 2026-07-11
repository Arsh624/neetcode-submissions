class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter={}
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        for i in counter.values():
            if i!=1:
                return True
        return False
            

        