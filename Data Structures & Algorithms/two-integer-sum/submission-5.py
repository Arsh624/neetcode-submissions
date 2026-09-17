class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        bruteforce 
        - check every pair  
        - for i in range(len(nums)):
            for j in range(1,len(nums))
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
            
        return []
        """
        
        hashm={}
        for i in range(len(nums)):# {3:0,4:1,5:2,6:3}
            hashm[nums[i]]=i
        
        for i in range(len(nums)):
            j=target-nums[i]
            if j in hashm and i!=hashm[j]:
                return [i,hashm[j]]
        return []
        

        
      

        

