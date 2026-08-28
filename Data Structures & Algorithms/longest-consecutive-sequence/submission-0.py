class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # see its simple , remove duplicates- > then just try to find the starting of a sequence ,not intermediates or nothing jsut the starting and then -> when you find starting -> just use while loop to check whether the next elelmet is in the set
        #coverting to set -> to get rid of duplicates
        numset=set(nums)
        longest=0
        for num in numset:
            
            if (num-1) not in numset:
                length=1

                while (num+length) in numset:
                    length+=1

                longest=max(length,longest)
        return longest
                




       
       
       
       
       
       
        # this is a brute force approach
        # nums.sort()
        # current=1
        # longest=1
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     elif nums[i]-nums[i-1]==1:
        #         current+=1
        #     else: 
        #         current=1
        #     longest=max(current,longest)

        # return longest