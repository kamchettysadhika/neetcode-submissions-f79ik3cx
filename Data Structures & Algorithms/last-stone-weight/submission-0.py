class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2 3 2 2]

        # [1 2 2]
        # [1 0]
        # [1]

        # [1,2]
        # [1]
         

        # three parts 
        # identfy the heaviest stones 
        # we need. to remove teh heaviest stones 
        # either absolute subtract 
        
        # or make them 0 if tehy are equal 
        # append the difference to the array 
        # then run the same algorthm on teh new array 
        # while len(stones) >1:
        # # sort  nlogn 
        # tehn pick teh last 2 elements  pop  O(1)
        # subtract both of them and append 
        
        # identifying 2 max elements removing them  
        # subtracting tehm and ten adding teh dfference to teh array until the 
        # length is 1  returning the last left element 
        #  [2,3,6,2,4]  
        stones = [-s for s in stones]  
        
        heapq.heapify(stones)
        
        while  len(stones) > 1: 
        #heapify array O(n)
            
          
            # maxheap pop O(1)pop two time 
            stone_1, stone_2 = heapq.heappop(stones),heapq.heappop(stones) 

            # subtract them O(1)
            heapq.heappush(stones,(stone_1 - stone_2))  
  
        return abs(stones[0])

        



