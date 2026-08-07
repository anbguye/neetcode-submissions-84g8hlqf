class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        cycles, visited = set(), set()
        res = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course):

            if course in cycles:
                return False
            
            if course in visited:
                return True
            
            cycles.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited.add(course)
            cycles.remove(course)
            
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res