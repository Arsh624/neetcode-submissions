class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)

        pre=1
        for i in range(len(nums)):
            output[i]=pre
            pre=pre*nums[i]

        suff=1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=suff
            suff=suff*nums[i]
        return output


        # output=[]
        # for i in range(len(nums)):
        #     prefix=nums[:i]
        #     suffix=nums[i+1:]
        #     output.append(math.prod(prefix+suffix))
        # return output
