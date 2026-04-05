class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       # row is sorte d
       # if at all we had to keep it in 1D then everything is sorted 
       """
       two parts 
       1) binary serach for the row 
       2) binary search for the element in teh row 
    
       """
       # 1) binary search for the row 
       top = 0 
       bot = len(matrix) - 1
       while top <= bot:
       
        row = (top+bot) //2 
        # now we check for ranges 
        # the element is nt in teh row if its greater than teh last elemnt or less than teh first element 
        if matrix[row][0] > target:
            bot = row - 1
        if matrix[row][-1] <target:
            top = row+1 
        else:
            break 

        if not top<= bot:
            return False 
      # search for teh elemnt in teh row 
       row = (top+bot) // 2
       l,r = 0, len(matrix[0])-1 
       while l<=r:
         m = (l+r)//2
         if matrix[row][m]>target:
             r = m-1
         elif matrix[row][m]<target:
             l = m+1
         else:
             return True 
       return False 
         




        

       