class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # 1-> number of bananans in the 1st pile 
        # 4-> Number of banas in teh second pile 
        # 3-> number of bananas in the third pile 
        # 2-> number of banans in the fourth pile 

        # h = number of hours you have 
        # k -> number odf banans you cna eat in a hour 
        # <k --> finish and stay idle for the rest 
        # minimum value of k so that you vcan eat all teh banans in an hour 
        l,r = 1, max(piles)
        res = r 
        
        while l<= r:
            m = (l+r)//2
            total_time = 0 
            for pile in piles:
                total_time += math.ceil(float(pile)/m) 
            if total_time > h:
                # we need to eat more banans 
                l = m+1 
            elif total_time <= h:
                res =m 
                r = m-1 
        return res
                # we need to eat less
