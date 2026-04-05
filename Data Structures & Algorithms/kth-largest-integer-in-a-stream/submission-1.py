class KthLargest:

    def __init__(self, k, nums):
       self.minHeap, self.k = nums, k
       #heapify
       heapq.heapify(self.minHeap)
       # store the maximum elements 
    #    while len(self.minHeap) > self.k:
    #     heapq.heappop(self.minHeap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val )
        while len(self.minHeap) >self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


       



   
    
   