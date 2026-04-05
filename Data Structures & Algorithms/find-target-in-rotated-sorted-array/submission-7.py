class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1 
        while l<=r:
            m = (l+r)//2 
            if target == nums[m]:
                return m
            if nums[l]<=nums[m]:
                #left part is sorted 
                if target <nums[l] or target >nums[m]:
                    l= m+1
                else:
                   r = m-1
            else:
                if target <nums[m] or target >nums[r]:
                   r=m-1
                else:
                    l=m+1
        return -1 


        # [3,4,5,6,1,2]
        # l.   m      r 
        # -> rotated 4 times 
        # l r
        # nums[m]>nums[r]:
        #     left part is sorted 
        # now if the target is between l and m search towards teh left 
        # if not search towards the right 
        # nums[m]<nums[r]:
        #     right part is sorted 
        #     so if target is between m to r then search towards right 
        #     else search towards the left 

