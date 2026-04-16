from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        In-place counting sort for values 0,1,2.
        Time: O(n)  Space: O(1) extra (counts only up to 3 keys).
        """
        # there are two parts 
        #1) keeping track of teh count 
        # here you can either use a hashmap or something else 
        # hashmap would be O(n) normally but if you flip it and have a list as a value and key is either 1,2,3
        # 0-> 3 
        # 1->1 
        # 2->2 
        # now instead of sorting it since we know taht there are only 3 keys possible what we can do is
        # we can hae 3 iterations 
        # 1 -> 0 
        # 2 -> 1 
        # 3-> 2 
        # at every iyteration we get the value of the i-1 elemnt and  overwrite tehy nums insdex value times 

        # construct a hashmap  
        # key -> 0,1,2 
        # value -> number of times 
        map = {0: 0,1:0,2:0}
        for num in nums:
            map[num] += 1
        index = 0 
        for i in range(3):
            while map[i]:
                map[i]-=1
                nums[index] = i 
                index+=1 

        #2) overwriting the array 