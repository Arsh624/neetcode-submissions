class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums - distinct
        search for target -> if it existes return index else -1
        """
        l , r = 0 , len(nums)-1
        while l <= r:
            #basecase 
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid+1
            else:
                r=mid-1
        return -1 
        