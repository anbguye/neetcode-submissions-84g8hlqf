class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid: 
            return -1

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q and fresh > 0:

            for i in range(len(q)):
                
                r, c = q.popleft()

                for dr, dc in dirs:

                    next_row, next_col = r + dr, c + dc

                    if min(next_row, next_col) < 0 or next_row == rows or next_col == cols or grid[next_row][next_col] == 0 or grid[next_row][next_col] == 2 or (next_row, next_col) in visited:
                        continue
                    
                    fresh -= 1
                    visited.add((next_row, next_col))
                    q.append((next_row, next_col))

            time += 1
        
        return time if fresh == 0 else -1