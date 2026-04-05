class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image 
        ROWS,COLS = len(image ),len(image[0])
        q = deque([(sr,sc)])
        image[sr][sc] = color
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in neighbors:
              if 0 <= dr + r < ROWS and 0 <= dc + c < COLS and image[dr+r][dc+c] == orig:
                    image[dr+r][dc+c] = color 
                    q.append((r+dr,c+dc))
        return image