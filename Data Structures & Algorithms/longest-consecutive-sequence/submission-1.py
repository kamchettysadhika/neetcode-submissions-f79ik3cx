class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set( nums)
        longest = 0 
        for number in numSet:
            if number-1 not in numSet:
                length = 1 
                while number+length in numSet:
                    length+=1 
                longest = max(length,longest )
        return longest
            