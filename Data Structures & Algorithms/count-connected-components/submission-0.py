class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        visited = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            for i in adj[node]:
                if i not in visited:
                    visited.add(i)
                    dfs(i)
        
        res = 0

        for i in range(n):

            if i not in visited:
                res += 1
                visited.add(i)
                dfs(i)
        
        return res

