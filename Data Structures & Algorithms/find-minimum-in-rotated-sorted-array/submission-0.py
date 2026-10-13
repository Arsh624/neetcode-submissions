class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        #problem: given arr of nums len n , rotated at ,return smallest element 
        #input: sorted array roated at k , unique
        #edge: empty-> return None , single->return it 
        #example: [ 3 , 4, 5, 6, 1 ,2 ] -> rotated 4 times 
        #approach: bruteforce - > search through an array -> O(n) O(1) 

        """
        #optimal
        left,right=0,len(nums)-1
        while left < right:
            mid= left + (right-left)//2 #5
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right=mid
        return nums[left]