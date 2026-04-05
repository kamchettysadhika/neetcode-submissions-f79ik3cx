class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        queue = deque([(0,0,1)]) # row,col,length
        visit = set((0,0))
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        while queue:
            r,c,l = queue.popleft()
            if ( min(r,c)<0 or max(r,c) >= ROWS or grid[r][c]):
                    continue
            if r == ROWS-1 and c == ROWS-1:
                return l
            for dr,dc in directions:
                if (r+dr,c+dc) not in visit:
                    queue.append((r+dr,c+dc,l+1))
                    visit.add((r+dr,c+dc))

        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #         Input: grid = [
#     [0,1,0],
#     [0,0,0],
#     [1,1,0]
# ]

# Output: 3
# if grid[0][0] or grid[1][1] == 1 then we acan return -1 
