class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l= 1
        r = 1
        while r <= len(nums)-1:
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
            r+=1
        return len(set(nums))
# [1,2,3,3,4]
#       write 
#      sliding

[1,2,3,4, 3]

                
            


