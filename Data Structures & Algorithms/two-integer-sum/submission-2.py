class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # core logic: at each number check if teh difference between the target and the num is in the array 
        # we can optimize the lookup by using a hashmap 
        # build a hashmap of num and idx 
        # there might be duplicates in tat case return the smaller idx 
        # build a hashmap for O(1) lookup 
        numIdx = {}
        for i,num in enumerate(nums):
            numIdx[num] = i 
        for idx,num in enumerate(nums):
            diff = target - num # diff can be negative in other case we search for negative number 
            if diff in numIdx and numIdx[diff] != idx:
                return [idx,numIdx[diff]]
        return []