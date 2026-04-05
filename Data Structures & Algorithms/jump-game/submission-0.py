class Solution:
    def canJump(self, nums: List[int]) -> bool:
       
        s = 0 
        maxReach = 0 
        while s < len(nums):
            if s > maxReach:
                return False
            maxReach =  max(s+ nums[s],maxReach)  
            if maxReach>= len(nums)-1:
                return True 
            s+=1 
        return True





