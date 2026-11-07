class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        """
        lout , rout = 0 , len(matrix)-1 
        while lout <=rout :
            mout = lout + (rout-lout)//2
            if target > matrix[mout][-1]:
                lout = mout + 1
            elif target < matrix[mout][0]:
                rout =mout-1
            else:
                break
        #this check is if we dont find anything in the above loop return false
        if not (lout <= rout):
            return False
        
        l,r=0 , len(matrix[mout])-1
        while l<=r:
            mid= l + (r-l)//2
            if matrix[mout][mid] < target:
                l = mid +1

            elif matrix[mout][mid] > target:
                r = mid -1
            else:
                return True

        return False

        