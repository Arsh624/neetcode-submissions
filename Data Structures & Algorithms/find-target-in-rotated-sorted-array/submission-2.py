class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        #problem - > given sorted rotated array at some pivot , return index  
        # input - > nums , sorted , rotated , target 
        # edge: empty-> atleast 1, return -1 if not found 
        # example: [ 4 , 5, 6, 7, 0 ,1 ,2 ] target=0 
                    l                    r
        # bruteforce o(n) -> binary search o(logn )
        """
        left , right = 0, len(nums) - 1
        while left <= right:
            mid= left + (right - left)//2  
            if nums[mid]==target:
                return mid
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
        return -1 
            
            

        