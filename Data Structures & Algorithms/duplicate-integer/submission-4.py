class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """brute force 
            - sort the array 
            - i=j-1 j=1
            - if i == j : return false
            - else return true
        """ 
        #optimal 
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            
            freq[nums[i]]=1
        return False
