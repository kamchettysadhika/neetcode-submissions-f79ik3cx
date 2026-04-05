class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited = set([(sr, sc)])
            steps = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        return steps

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if not (0 <= nr < ROWS and 0 <= nc < COLS):
                            continue
                        if grid[nr][nc] == -1:
                            continue
                        if (nr, nc) in visited:
                            continue

                        visited.add((nr, nc))
                        q.append((nr, nc))

                steps += 1

            return INF  # no treasure reachable

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)