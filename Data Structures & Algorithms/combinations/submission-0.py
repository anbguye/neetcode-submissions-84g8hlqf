class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        curr = []
        res = []

        def dfs(i, n, k):

            if len(curr) >= k:
                res.append(curr.copy())
                return

            if i > n:
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                dfs(j + 1, n, k)
                curr.pop()
        
        dfs(1, n, k)
        return res