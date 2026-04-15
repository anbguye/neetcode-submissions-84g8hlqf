class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        adj = defaultdict(list)

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        res = 0

        def dfs(node):
            for nei in adj[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
    
        return res