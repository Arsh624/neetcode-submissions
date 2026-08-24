class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm={}
        for i in range(len(nums)):
            hashm[nums[i]]=i
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashm and hashm[diff]!=i:
                return [i,hashm[diff]]
        return False
