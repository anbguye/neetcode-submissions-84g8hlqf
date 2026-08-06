class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        visited = set()

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        def dfs(course):

            if course in visited:
                return False

            if graph[course] == None:
                return True
            
            visited.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            visited.remove(course)
            graph[course] = None
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True