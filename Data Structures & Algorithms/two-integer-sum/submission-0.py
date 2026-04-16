class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3 4 5 6]
        # target = 7 

        # find two numbers that sum up to the target and alo the indices are not teh same 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums))

        #     [ 3 4 5 6 ]
        #         l.  r 
        # [34563]
        #building the map 
        numMap = {}
        for idx,num in enumerate(nums):
            numMap[num] = idx
        for i,n in enumerate(nums):
            diff = target- n
            if diff in numMap and numMap[diff]!= i:
                    return [i,numMap[diff]]
        return []