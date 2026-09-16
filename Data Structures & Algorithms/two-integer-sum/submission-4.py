class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm={}
        for i in range(0,len(nums)):
            hashm[nums[i]]=i
        for i in range(0,len(nums)):
            find=target-nums[i]
            if find in hashm and hashm[find]!=i:
                return [i,hashm[find]]
        
            # {3:0,4:1,5:2,6:3}

        

