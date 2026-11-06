class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        input=-> numbers sorted in ascending order
        output-> [ index1, index2] such that n1+n2 = target and index 1 < index2 and index 1 != index 2 

        numbers= [1 ,2, 3, 4] target = 3  
        """
        i , j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1
        return []






















        # l,r=0,len(numbers)-1
        # while l<r:
        #     if numbers[l]+numbers[r]==target:
        #         return [l+1,r+1]
        #     elif numbers[l]+numbers[r]>target:
        #         r-=1
        #     else:
        #         l+=1
        # return []
        