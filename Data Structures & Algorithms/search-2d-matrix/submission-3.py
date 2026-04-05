class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       # row is sorte d
       # if at all we had to keep it in 1D then everything is sorted 
       ROWS = len(matrix)
       COLS = len(matrix[0])
       for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == target:
                return True 
       return False