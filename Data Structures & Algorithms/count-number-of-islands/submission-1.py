class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not any("1" in row for row in grid):
            return 0


        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c< 0 or grid[r][c] == "0":
                return      
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1 
        return islands
                

            

#         Input: grid = [
#     ["0","1","0","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1

