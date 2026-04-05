class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsCopy = nums.copy()
        numsCopy.extend(nums)
        return numsCopy
    