class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0 
        prefix = {0:1} # base case of 0 
        for num in nums:
            curSum += num  # compute teh sum till now 
            diff = curSum - k  # compuyte teh diff between till now and teh target 
            
            res += prefix.get(diff, 0)
            prefix[curSum]= 1+  prefix.get(curSum, 0)
            

        return res


    # we are basically doing number of ways to remove a prefixsum of x
    # and tehn computing teh diff at each number then computing teh result as 
    # or incrementung teh result by number of ways we can remove that diff prefix 



