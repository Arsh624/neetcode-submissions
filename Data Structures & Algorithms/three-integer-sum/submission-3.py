class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        input->nums = [-1,0,1,2,-1,-4]
        output-> return all triplets - > [ [-1,-1,2] , [-1,0,1]]
        edge->
        """

        # -4 , -1 , -1 , 0 , 1 ,2
        res= []
        nums.sort()
        for i , num in enumerate(nums):
            #we have already processed the 0th index - so if 1st ind = 0th weskip
            if i > 0 and num==nums[i-1]:
                continue
            l,r = i+1 , len(nums)-1
            while l < r:
                tsum= num + nums[l] + nums[r]
                if tsum > 0:
                    r-=1
                elif tsum < 0:
                    l+=1

                else:
                    res.append([num, nums[l] ,nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res






















        # res=[]
        # nums.sort()
        # for i,a in enumerate(nums):
        #     if i > 0 and a==nums[i-1]:
        #         continue 

        #     l,r= i+1 , len(nums)-1
        #     while l < r:
        #         tsum=a+nums[l]+nums[r]
        #         if tsum>0:
        #             r-=1
        #         elif tsum <0:
        #             l+=1
        #         else:
        #             res.append([a,nums[l],nums[r]])
        #             l+=1
        #             while nums[l] == nums[l-1] and l<r:
        #                 l+=1
        # return res

             
        