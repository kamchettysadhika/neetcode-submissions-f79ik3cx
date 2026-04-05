class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1 
        sliding = 1
        while sliding <= len(nums)-1:
            if nums[sliding] != nums[sliding-1]:
                nums[write] = nums[sliding]
                write+=1 
            sliding+=1
        return len(set(nums))
