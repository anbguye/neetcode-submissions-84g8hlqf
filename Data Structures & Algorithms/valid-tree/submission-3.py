class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True
        
        adj = defaultdict(list)

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()

        def dfs(curr, prev):

            if curr in visited:
                return False
            
            visited.add(curr)
            
            for node in adj[curr]:

                if node == prev:
                    continue
                
                if not dfs(node, curr):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n