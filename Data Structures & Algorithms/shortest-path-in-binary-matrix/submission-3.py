class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        length = 1
        visited = set([(0,0)])
        q = deque([(0, 0)])

        while q:

            for i in range(len(q)):

                r, c = q.popleft()


                if r == rows - 1 and c == cols - 1:
                    return length
                
                directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

                for dx, dy in directions:

                    nr, nc = r + dx, c + dy
                    
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))
                
            length += 1

        return -1