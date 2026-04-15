class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        visited = set()

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node, prev):

            if node in visited:
                return False
            
            visited.add(node)
            
            for nei in adj[node]:
                if nei == prev:
                    continue
                
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and n == len(visited)