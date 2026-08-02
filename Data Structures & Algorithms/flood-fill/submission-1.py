class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image

        rows, cols = len(image), len(image[0])
        beginning_color = image[sr][sc]

        def dfs(r, c):

            if min(r,c) < 0 or r == rows or c == cols or image[r][c] != beginning_color:
                return
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image