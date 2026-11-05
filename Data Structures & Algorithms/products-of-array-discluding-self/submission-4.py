class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        see build prefix multiplicaiton array 
        then build suffix multipli array 
        output is (prefix * suffix) 
        """
        # [ 1 , 1 , 1 , 1 ]
        # [ 1 , 2 , 4 , 6 ]
        res = [1]* len(nums)
        pre= 1
        for i in range(len(nums)):
            res[i] = pre  # 1 1 2 8
            pre= pre * nums[i]
        suff= 1
        for i in range(len(nums)-1, -1,-1):
            res[i]= res[i]* suff
            suff = suff * nums[i]
        return res


        
        # output=[1]*len(nums)
        
        # pre=1
        # for i in range(len(nums)):
        #     output[i]=pre
        #     pre=pre*nums[i]
        # [1 1 2 8]
        # [1]
        # suff=1
        # for i in range(len(nums)-1,-1,-1):
        #     output[i]*=suff
        #     suff=suff*nums[i]
        # return output


        # output=[]
        # for i in range(len(nums)):
        #     prefix=nums[:i]
        #     suffix=nums[i+1:]
        #     output.append(math.prod(prefix+suffix))
        # return output
