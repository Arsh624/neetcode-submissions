class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm={}
        for i in range(0,len(nums)):
            hashm[nums[i]]=i 
        
        for i in range(0,len(nums)):
            comp=target-nums[i]
            if comp in hashm and hashm[comp]!=i:
                return [i,hashm[comp]]
            
