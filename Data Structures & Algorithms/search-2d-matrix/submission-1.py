class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        top = 0
        bot = ROW - 1
        while top <= bot:
            m = (top+bot)//2
            if target > matrix[m][-1]:
                top = m+1
            elif target < matrix[m][0]:
                bot = m-1
            else:
                break 
        if not(top <= bot):
            return False 
        row = (top+bot)//2
        COL = len(matrix[0])
        left,right = 0, COL - 1
        while left <= right:
            m = (left+right)//2
            if target > matrix[row][m]:
                left = m+1
            elif target < matrix[row][m]:
                right = m-1 
            else:
                return True
        return False