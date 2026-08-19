class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build the prefix array 
        # build teh suffix array 
        # multiply both of them 
        #1) build teh prefic array 
        n = len(nums)
        
        res = [1] * n 
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i]= prefix 
            prefix = prefix* nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]* postfix
            postfix = postfix * nums[i]
        return res 

