class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0 
        def dfs(r,c):

            if r< 0 or c <0 or r >= ROWS or c >= COLS or grid[r][c]==0:
                return 0 
            grid[r][c] = 0 
               # visit.add(r,c)
            return (1+ dfs(r,c+1)+
            dfs(r,c-1)+
            dfs(r+1,c)+
            dfs(r-1,c))
        
        for i in range(ROWS):
            for j in range(COLS):
                area = max(area,dfs(i,j))
        return area

        

        # find the islannds 
        # count the island's path 
        # max(count)

#         Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],  
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ].    


        # [1] - 1 
        # [0] - 0 
