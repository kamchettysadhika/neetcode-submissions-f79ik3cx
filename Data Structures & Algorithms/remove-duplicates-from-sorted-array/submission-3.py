class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        slide  = 0

        while slide <len(nums):
            nums[write] = nums[slide]
            while slide <len(nums) and nums[write] == nums[slide]:
                slide+=1
            write += 1
        return len(set(nums))
       
            

            

# [1,2,3,3,4]
#       write 
#      sliding

# [1,2,3,4, 3]

#         # [1,1,1, 1, 2,3,4]
        
#                write pointer and a sliding pointer 
#             so a write pointer would keep track of the duplicate elemnt and the sliding pointer will keep track of the new elemnt 


# # because the input is sorted the two duplicate elements will be next to each other 
# # we can use this to our advantage 
# # we have to move our second one and shift all the elents to the left 
# # we basically have to overwrit ethe second one 
# # 1) find teh duplicate elet or find where teh element has been occuring for the second time 
# # and from there go to